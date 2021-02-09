if [ "1" == "test" ]; then #@1
	exit - #@2
fi #@3
MANAGER=(test cd ls pwd) #@4
RANDOM=$$ #@5
for target in *; do #@6
		nbline=$(wc -l $target)
		nbline=${nbline##}
		nbline=$(echo $nbline | cut -d "" -f1)

