<?php
  function get_url($url)
  {
    // Initialize a CURL session.
    $ch = curl_init();
    // Return Page contents.
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    //grab URL and pass it to the variable.
    curl_setopt($ch, CURLOPT_URL, $url);
    $result = curl_exec($ch);
    return($result);
  }

  function post_url($url)
  {
    $ch = curl_init();
    // Return Page contents.
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    //grab URL and pass it to the variable.
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    $result = curl_exec($ch);
    return($result);
  }
?>
