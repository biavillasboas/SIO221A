variable='temperature'
cd ../data/sccoos_sio_pier
files=`ls -1 *.nc | awk '{print $1}' ORS=' '`
`ncrcat -v ${variable} $files ${variable}_sccoos_sio_pier_2005_2019.nc`
