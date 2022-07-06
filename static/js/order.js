console.log("i am from order");

// // var cart = [];
// var lclCheck = localStorage.getItem('CART');
// var cart = lclCheck ? JSON.parse(lclCheck) : [];



function renderOrderPage() {
    orderBody.innerHTML = "";
    cart.forEach((element, index) => {
        orderBody.innerHTML += `
            <tr >
                <td class="p-4 fw-light">${element.product_name} <span>&#x2716;</span> ${element.quntity}</td>
                <td class="p-4 fw-light">${element.quntity * element.price}</td>
            </tr>
        `;
    });
    orderBody.innerHTML += `
            <tr>
                <td class="p-4 fw-bold">Subtotal:</td>
                <td class="p-4 fw-bold" id="orderSubtotal">0</td>
            </tr>
            <tr>
                <td class="p-4 fw-bold">Shipping:</td>
                <td class="p-4 fw-bold">50</td>
            </tr>
            <tr>
                <td class="p-4 fw-bold">Total:</td>
                <td class="p-4 fw-bold" id="orderTotal">0</td>
            </tr>
    `;

    // document.querySelector(".cart-details").insertAdjacentHTML("beforeend", html);
}

window.addEventListener('DOMContentLoaded', (event) => {
    // renderOrderPage();
    // subTotal();
});


// function subTotal(){
//     var totalPrice = 0;
//     var totalItem = 0;

//     cart.forEach((element,index)=>{
//         totalPrice += (element.price * element.quntity);
//         totalItem += element.quntity;
//     })
    
//     // cartSubtotal.innerText = `${totalPrice} (${totalItem} items)`;
//     orderSubtotal.innerText = `${totalPrice}`;
//     orderTotal.innerText = `${totalPrice+50}`;
//     // if(totalPrice>0){
//     //     orderTotal.innerText = `${totalPrice+50}`;
//     //     // shippingPrice.innerText = 50;
//     // }else{
//     //     orderTotal.innerText = 0;
//     //     // shippingPrice.innerText = 0;
//     // }


//     // cartIcon.innerText = totalItem;
//     // cartIconMb.innerText = totalItem;

// }



















