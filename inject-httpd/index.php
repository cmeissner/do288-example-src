<?php
$name = getenv("NAME") != '' ? getenv("NAME") : 'world' ;
echo 'Hello ' . $name . '!';
?>
