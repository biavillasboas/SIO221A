mkdir ../data/sccoos_sio_pier
cd ../data/sccoos_sio_pier
for year in `seq -w 5 19`
do
wget http://sccoos.org/thredds/fileServer/autoss/scripps_pier-20${year}.nc
done
