
with open('data.csv') as infile, open('data_no_nd.csv', 'w') as outfile:
	prev_line = None
	for line in infile:
		tokens = line.split(',')[:-1]
		if 'ND' in ','.join(tokens):
			if prev_line is not None:
				prev_tokens = prev_line.split(',')[:-1]
				tokens = [tokens[0]] + prev_tokens[1:]
				print('ND observed, tokens: ', tokens, ', prev_tokens:', prev_tokens)
			else:
				continue
		else:
			prev_line = line

		line_out = ','.join(tokens) + '\n'

		outfile.write(line_out)
