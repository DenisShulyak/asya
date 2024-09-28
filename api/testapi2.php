<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type");
header("Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS");
header('Content-Type: application/json; charset=utf-8');


if (!isset($_GET['CODE'])) {
    $result = ['result' => 'Parameters {CODE} not found in get request', 'status' => '400'];
    echo json_encode($result);
    return;
}

$aData = [
  'Andrologia' => [
           'section' => 'Андрология',
           'items' => [
               [
              'id' => 1,
              'code' => 'N30.2',
              'name' => 'Другой хронический цистит'
               ],
               [
              'id' => 2,
              'code' => 'N31.2',
              'name' => 'Другой хронический цистит1'
               ],
               [
              'id' => 3,
              'code' => 'N31.3',
              'name' => 'Другой хронический цистит2'
               ],
            ]
       ], 
    'Popular diagnoses' => [
        'section' => 'Популярные диагнозы',
           'items' => [
               [
                  'id' => 4,
                  'code' => 'N30.2',
                  'name' => 'Другой хронический цистит'
               ],
               [
                  'id' => 5,
                  'code' => 'N31.2',
                  'name' => 'Другой хронический цистит1'
               ],
               [
                  'id' => 6,
                  'code' => 'N31.3',
                  'name' => 'Другой хронический цистит2'
               ],
            ]
    ],
    'Dermatology' => [
    'section' => 'Дерматология',
           'items' => [
               [
              'id' => 7,
              'code' => 'N30.2',
              'name' => 'Другой хронический цистит'
               ],
               [
              'id' => 8,
              'code' => 'N31.2',
              'name' => 'Другой хронический цистит1'
               ],
               [
              'id' => 9,
              'code' => 'N31.3',
              'name' => 'Другой хронический цистит2'
               ],
            ]
    ],
    'Therapy' => [
    'section' => 'Терапия',
           'items' => [
               [
              'id' => 10,
              'code' => 'N30.2',
              'name' => 'Другой хронический цистит'
               ],
               [
              'id' => 11,
              'code' => 'N31.2',
              'name' => 'Другой хронический цистит1'
               ],
               [
              'id' => 12,
              'code' => 'N31.3',
              'name' => 'Другой хронический цистит2'
               ],
            ]
    ],
   ];
   
if (!isset($aData[$_GET['CODE']])) {
     $result = ['result' => 'Not found items', 'status' => '404'];
    echo json_encode($result);
    return;
}

$result = ['result' => json_encode($aData[$_GET['CODE']]), 'status' => '200'];
echo json_encode($result);
