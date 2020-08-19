// var total = {{order.get_cart_total|floatformat:2}}

var csrftoken = getToken('csrftoken')
var form = document.getElementById('form')
form.addEventListener('submit', function(e){
e.preventDefault()
console.log('Form Submitted...')
document.getElementById('form-button').classList.add("hidden");
document.getElementById('payment-info').classList.remove("hidden");
})

document.getElementById('make-payment').addEventListener('click', function(e){
submitFormData()
})

function submitFormData(){
console.log('Payment button clicked')

 var userFormData = {
          'name':null,
          'phonenumber':null,
     }

//       var shippingInfo = {
//           'address':null,
//           'city':null,
//           'state':null,
//           'zipcode':null,
//      }
//
//      if (shipping != 'False'){
//      shippingInfo.address = form.address.value
//      shippingInfo.city = form.city.value
//      shippingInfo.state = form.state.value
//      shippingInfo.zipcode = form.zipcode.value
// }


userFormData.name = form.name.value
userFormData.phonenumber = form.phonenumber.value

// console.log('Shipping Info:', shippingInfo)
// console.log('User Info:', userFormData)

var url = "/process_order/"
fetch(url, {
     method:'POST',
     headers:{
          'Content-Type':'applicaiton/json',
          'X-CSRFToken':csrftoken,
     },
     body:JSON.stringify({'form':userFormData }),

})
.then((response) => response.json())
.then((data) => {
          console.log('Success:', data);
          alert('Transaction completed');

          cart = {}
          document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

          window.location.href = "{% url 'store' %}"

          })
}
