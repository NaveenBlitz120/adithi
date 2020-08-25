var updateBtns = document.getElementsByClassName('update-cart')
// var check = document.getElementsByClassName('added')

for (let i = 0; i < updateBtns.length; i++) {
	// console.log(updateBtns[i].dataset.product,'here')

	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var type = this.dataset.type
		var page = this.dataset.page
		
		console.log(check);
		// console.log('productId:', productId, 'Action:', action, 'Type:',type)
		// console.log('USER:', user)
		if(type == 'flower')
		{
			var category = this.dataset.category
			addflowerItem(productId,action,category)
		}
		else {
			if(page == 'home')
			{
				var check = document.getElementById(productId).value
			}
			addCookieItem(productId, action ,type,check)
		}

	})
}

function addCookieItem(productId, action, type,check){
	// console.log('User is not authenticated')


			console.log('productId:', productId, 'Action:', action, 'Type:',type);
			console.log('USER:', user);
	if (action == 'add'){
		if (cart[productId] == undefined){
			// check=check*1
			console.log('entered',(check));
			console.log('entered',typeof(check));
			if (type == 'flower')
			{
				console.log({productId});
			}
			if((type == 'kg') || (type == 'grams'))
			{
				if (check=='250'||check=='500'||check=='750')
				{
					console.log('entered',check);
					cart[productId] = {'quantity':(check/1000)};
				}
				else if (type == 'kg'){
					cart[productId] = {'quantity':1};
				}
				else{
					cart[productId] = {'quantity':.1};
				}

			}
			else
			{
				cart[productId] = {'quantity':1	};
			}
		}
		else
		{
			if (type == 'count')
			{
				cart[productId]['quantity'] += 1
			}
			else
			{
				if (check=='250'||check=='500'||check=='750')
				{
					console.log('entered',check);
					cart[productId]['quantity'] += (check/1000);
				}
				else {
					cart[productId]['quantity'] += .100
				}
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


function addflowerItem(productId, action, category){
	// console.log('User is not authenticated')


			console.log('productId:', productId, 'Action:', action,'flower');
			console.log('USER:', user);
	if (action == 'add'){
		if (flower[productId] == undefined)
		{
			if((category == 'kg') )
			{
				flower[productId] = {'quantity':1}
			}
			else if (category == 'grams')
			{
				flower[productId] = {'quantity':.1}
			}
			else
			{
				flower[productId] = {'quantity':1};
			}
		}
		else
		{
			if ((category == 'grams') || (category == 'kg'))
			{
				flower[productId]['quantity'] += .1
			}
			else
			{
				flower[productId]['quantity'] += 1
			}
			flower[productId]['quantity'] = parseFloat(flower[productId]['quantity'].toPrecision(3))

		}
	}
	if (action == 'remove'){
		if ((category == 'grams') || (category == 'kg')){
			flower[productId]['quantity'] -= .1;
		}
		else {
			flower[productId]['quantity'] -= 1;
		}
		flower[productId]['quantity'] = parseFloat(flower[productId]['quantity'].toPrecision(3))

		if (flower[productId]['quantity'] < .100){
			console.log('Item should be deleted');
			delete flower[productId];
		}
	}
	console.log('flower', flower);
	document.cookie ='flower=' + JSON.stringify(flower) + ";domain=;path=/"

	location.reload();
}
