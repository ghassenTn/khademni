
    <?php
    $username ="localhost";
    $password ="";
    $database = new PDO("mysql:host=localhost; dbname=test;charset=utf8;",$username,$password);
    if($database)
    {
        echo 'ok' ;
    }
    ?>

