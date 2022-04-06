<?php
    global $file;
    
    function getDateTime(){
        date_default_timezone_set('EST');
        return date("m/d/y h:i:s a", $_SERVER['REQUEST_TIME']);
    }
    
    
    
    function readCSV($filename){
        $file = fopen($filename, "r+");
        $ret = array();
        $i = 0;
        while(($data= fgetcsv($file)) !== FALSE){
            $ret[$i] = $data;
            $i++;
        }

        fclose($file);
        return $ret;
    }

    function wipeCSV($filename){
        $file = fopen($filename, "w");
        $a = array();
        fputcsv($file, $a);
        fclose($file);
    }

    function appendCSV($filename, $data){
        $file = fopen($filename, "a+");
        fputcsv($file, $data);
        fclose($file);
    }



?>