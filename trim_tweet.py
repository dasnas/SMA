import json
delete_list = ["id","source","in_reply_to_status_id","in_reply_to_user_id","in_reply_to_screen_name","coordinates","place","quoted_status_id","is_quote_status","extended_entities","matching_rules","filter_level","possibly_sensitive","retweeted","favorited"]
def trim(tw,dl):
	#delete_list = ["id","source","in_reply_to_status_id","in_reply_to_user_id","in_reply_to_screen_name","coordinates","place","quoted_status_id","is_quote_status","extended_entities","matching_rules","filter_level","possibly_sensitive","retweeted","favorited"]
	for t in tw:
		for x in dl:
			t.pop(x,None)
	return tw

def main():
	with open("60940448tweets.json",'r') as uf:
		tw = json.load(uf)
	trim(tw,delete_list)
	with open("check.json",'w') as f:
		json.dump(tw,f,indent=4)

if __name__ == '__main__':
	main()