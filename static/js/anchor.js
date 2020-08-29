var fruits = {% url 'fruits' %}
document.querySelector(".category-1").setAttribute('onclick', 'location.href = fruits');
document.querySelector(".category-2").setAttribute('onclick', 'location.href = "vegetables"');
document.querySelector(".category-3").setAttribute('onclick', 'location.href = "groceries"');
document.querySelector(".category-4").setAttribute('onclick', 'location.href = "flowers"');
