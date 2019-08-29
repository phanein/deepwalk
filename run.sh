#!/bin/bash
#
# \description  Execution on multiple networks
#
# \author Artem V L <artem@exascale.info>  https://exascale.info

DIMS=128
NETS="blogcatalog dblp homo wiki youtube"
WORKERS=8
RESTRACER=./exectime  # time
LOGDIR=embeds/logs
mkdir -p $LOGDIR

USAGE="$0 -h | [-d <dimensions>=${DIMS}] [-w <workers>=${WORKERS}]
  -d,--dims  - required number of dimensions in the embedding model
  -w,--workers  - maximal number of workers (parallel thread). Note: deepwalk training can be failed on non-small datasets with small number of workers
  -h,--help  - help, show this usage description

  Examples:
  \$ $0 -d 128 -w 4
"

while [ $1 ]; do
	case $1 in
	-h|--help)
		# Use defaults for the remained parameters
		echo -e $USAGE # -e to interpret '\n\
		exit 0
		;;
	-d|--dims)
		if [ "${2::1}" == "-" ]; then
			echo "ERROR, invalid argument value of $1: $2"
			exit 1
		fi
		DIMS=$2
		echo "Set $1: $2"
		shift 2
		;;
	-w|--workers)
		if [ "${2::1}" == "-" ]; then
			echo "ERROR, invalid argument value of $1: $2"
			exit 1
		fi
		WORKERS=$2
		echo "Set $1: $2"
		shift 2
		;;
	*)
		printf "Error: Invalid option specified: $1 $2 ...\n\n$USAGE"
		exit 1
		;;
	esac
done

for NET in $NETS; do
	$RESTRACER python3 -m deepwalk --format mat --input  graphs/${NET}.mat --number-walks 80 --representation-size ${DIMS} --walk-length 40 --window-size 10 --workers $WORKERS --output embeds/embs_${NET}_${DIMS}-n80-l40-s10.w2v > "$LOGDIR/${NET}_${DIMS}-n80-l40-s10.log" 2> "$LOGDIR/${NET}_${DIMS}-n80-l40-s10.err" # &
done
# python3 -m deepwalk --format mat --input example_graphs/blogcatalog.mat --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/blogcatalog.w2v
