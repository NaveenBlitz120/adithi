var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	console.log('entred')
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var type = this.dataset.type

		// console.log('productId:', productId, 'Action:', action, 'Type:',type)
		// console.log('USER:', user)

		addCookieItem(productId, action ,type)

	})
}
function addCookieItem(productId, action, type){
	// console.log('User is not authenticated')


			console.log('productId:', productId, 'Action:', action, 'Type:',type);
			console.log('USER:', user);
	if (action == 'add'){
		if (cart[productId] == undefined){
			if((type == 'kg') || (type == 'count'))
			{
				cart[productId] = {'quantity':1};
			}
			else
			{
				cart[productId] = {'quantity':.100};
			}
		}
		else
		{
			if((type == 'grams'))
			{
				console.log(cart[productId]['quantity']);
				cart[productId]['quantity'] += .100;
				cart[productId]['quantity'] = parseFloat(cart[productId]['quantity'].toPrecision(3))
				console.log(cart[productId]['quantity']);
			}
			else if (type == 'count')
			{
				cart[productId]['quantity'] += 1
			}
			else
			{
				cart[productId]['quantity'] += .100
				cart[productId]['quantity'] = parseFloat(cart[productId]['quantity'].toPrecision(3))
			}

		}
	}

	if (action == 'remove'){
		if (type == 'count') {
				cart[productId]['quantity'] -= 1;
		}
		else {
			cart[productId]['quantity'] -= .100;
			cart[productId]['quantity'] = parseFloat(cart[productId]['quantity'].toPrecision(3))
		}

		if (cart[productId]['quantity'] < .100){
			console.log('Item should be deleted');
			delete cart[productId];
		}
	}
	console.log('CART:', cart);
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload();
}
