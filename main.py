import requests, argparse, json

parser = argparse.ArgumentParser() #Set up command line arguments
parser.add_argument('-n', '--num', type=int, default=1, help='Specifies the number of results to return')
parser.add_argument('-r', '--random', help='Return random result', action='store_true')
parser.add_argument('-a', '--all', help='Return all results', action='store_true')
parser.add_argument('word', nargs='?', help='Word used in query')
args = parser.parse_args()

define_url = 'http://api.urbandictionary.com/v0/define?term='
random_url = 'http://api.urbandictionary.com/v0/random'

def retry(r, url): #Retry until hitting retry limit
	retry = 3
	for i in range(retry):
		if r.status_code == 200:
			return json.loads(r.text)
		elif r.status_code == 503:
			print('Request timed out, retrying...')
			r = requests.get(url)

	if r.status_code == 503:
		print('Retry timeout exceeded')
		exit()

def print_defs(result, num): #Print information about the words
	print('\n==================================\n')
	for i in range(0, num): #This will print "args.num" definitions
		#Prettify
		print('Word:\n\n\t', end='')
		print(result['list'][i]['word'].replace('\n', '\n\t'))
		print()
		print('Author:\n\n\t', end='')
		print(result['list'][i]['author'].replace('\n', '\n\t'))
		print()
		print('Definition:\n\n\t', end='')
		print(result['list'][i]['definition'].replace('\n', '\n\t'))
		print()
		print('Example:\n\n\t', end='')
		print(result['list'][i]['example'].replace('\n', '\n\t'))
		print()
		print('Rating:\t{}'.format(str(int(result['list'][i]['thumbs_up']) - int(result['list'][i]['thumbs_down']))))
		print('\n==================================\n')

try: #Handle CTRL+C
	if not args.random: #Determine to print random, or specific def
		r = requests.get('{}{}'.format(define_url, args.word))
		result = retry(r, '{}{}'.format(define_url, args.word))
	else:
		r = requests.get(random_url)
		result = retry(r, random_url)

	if not args.all: #Determine to print all or certain amount of defs
		print_defs(result, args.num)
	else:
		print_defs(result, len(result['list']))

except KeyboardInterrupt:
	print()
	exit()