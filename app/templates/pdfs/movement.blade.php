<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <table class="table table-bordered">
    <thead>
      <tr>
        <td><b>Show Name</b></td>   
      </tr>
      </thead>
      <tbody>
      @foreach($movement_products as $movement_product)
      <tr>
        <td>
          {{ $movement_product->movement_product_id }}
        </td>
      </tr>
      @endforeach
      </tbody>
    </table>
  </body>
</html>