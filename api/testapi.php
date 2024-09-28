<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type");
header("Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS");
header('Content-Type: application/json; charset=utf-8');


$aItems = [
  ['name'=> 'Популярные диагнозы', 'code' => 'Popular diagnoses', 'itemsCount' => 18],
  ['name'=> 'Андрология', 'code' => 'Andrologia', 'itemsCount' => 18],
  ['name'=> 'Дермотология', 'code' => 'Dermatology', 'itemsCount' => 18],
  ['name'=> 'Терапия', 'code' => 'Therapy', 'itemsCount' => 7],
];


echo json_encode($aItems);