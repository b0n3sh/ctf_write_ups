#!/usr/bin/python3
import json
from collections import Counter

ip = '251.71.156.29'

def avg(x):
	return sum(x) / len(x)

with open('incidents.json') as incidents_:
	incidents = json.load(incidents_)['tickets']

	
	dst_ip = {}
	file_hash = {}

	def get_first_question():
		src_ip = Counter()
		for incident in incidents:
			src_ip[incident['src_ip']] += 1
		return src_ip.most_common()
		

	def get_second_question(ip):
		# For getting unique ips, we will be using sets.
		src_ip = set()
		for incident in incidents:
			if incident['src_ip'] == ip:
				src_ip.add(incident['dst_ip'])
		return len(src_ip)

	def get_third_question():
		dst_ip = {}
		for incident in incidents:
			if incident['file_hash']in dst_ip:
				if [incident['dst_ip']] not in dst_ip.values():
					dst_ip[incident['file_hash']].append(incident['dst_ip'])
			else:
				dst_ip[incident['file_hash']] = [incident['dst_ip']]

		return [len(x) for x in dst_ip.values()]

# First question
print(f'The most common source IP address is {get_first_question()[0][0]} with {get_first_question()[0][1]} repetitions.')

# Second question
print(f'The IP {ip} has {get_second_question(ip)} unique destination IP addresses.')

# Third question
print(f'The average number of unique destination ips a file is sent is {round(avg(get_third_question()), 2)}')
