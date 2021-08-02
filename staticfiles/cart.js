function AddToCart(product_id){
    let count = document.getElementById('quantity').value;
    console.log(count)
    let d = {
        product_id:product_id,
        count:count,
    }
    let data = JSON.stringify(d)

	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      var data = JSON.parse(this.responseText);
      if (data['status'] === 200){
          var block = document.getElementById('info');
          block.classList = ['message info-show']
      }
    }else{
      console.log('not yet')

      }
    }

    var url = "/cart/add/"
    xhttp.open("GET", url+`?data=${data}`, true);
    xhttp.send();
}
