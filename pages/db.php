<?php
$id = $_POST['id'];
$nom = $_POST['nom'];
    $username ="patchnet";
    $password ="";
    $database = new PDO("mysql:host=localhost; dbname=2ligbi;charset=utf8;",$username,$password);
    if($database->connect_error) {
       die ('connection failed : '.$database->connect_error);

    }else
        $stmnt = $database->prepare("insert into 2ligbi(id,nom) values (?,?)");
    $stmnt->bindParam("is",$id,$nom);
    echo 'registry successful';
    $stmnt->close();
    $database->close();



    ?>

