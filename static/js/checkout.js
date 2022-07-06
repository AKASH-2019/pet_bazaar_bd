console.log("from checkout");

var lclCheck = localStorage.getItem('CART');
var cart = lclCheck ? JSON.parse(lclCheck) : [];

document.getElementById("orderBtn").addEventListener("click",async (e)=>{
    e.preventDefault();
    
    
    if(document.getElementById("inputEmail").value.length == 0){
        document.getElementById("inputEmail").style.borderColor = "red";
        return;
    }
    else{
        document.getElementById("inputEmail").style.borderColor = "#ced4da";
    }
    if(document.getElementById("inputPhone").value.length == 0){
        document.getElementById("inputPhone").style.borderColor = "red";
        return;
    }
    else{
        document.getElementById("inputPhone").style.borderColor = "#ced4da";
    }
    if(document.getElementById("inputDistrict").value.length == 0){
        document.getElementById("inputDistrict").style.borderColor = "red";
        return;
    }
    else{
        document.getElementById("inputDistrict").style.borderColor = "#ced4da";
    }
    if(document.getElementById("inputCity").value.length == 0){
        document.getElementById("inputCity").style.borderColor = "red";
        return;
    }
    else{
        document.getElementById("inputCity").style.borderColor = "#ced4da";
    }
    if(document.getElementById("inputStreet").value.length == 0){
        document.getElementById("inputStreet").style.borderColor = "red";
        return;
    }
    else{
        document.getElementById("inputStreet").style.borderColor = "#ced4da";
    }
    
    var totalPrice = 0;
    cart.forEach((element,index)=>{
        totalPrice += (element.price * element.quntity);
    })

    var frm = new FormData(document.getElementById("orderForms")); 
    frm.append("total_price",totalPrice);
    frm.append("order_item",lclCheck);
    // frm.forEach(element => {
    //     console.log(element);
    // });

    var data = await fetch('/orderUpsert',{
        method: 'post',
        body: frm
    });

    var res = await data.json();
    console.log(res);
    if(res[0]["order_id"] > 0 && res[0]["order_details"]["order_details_id"] > 0){
        localStorage.clear();
        window.location = `/order/${res[0]["order_id"]}`;
    }
})

// form validation
// (function() {
//     'use strict';
//     window.addEventListener('load', function(e) {
//         e.preventDefault();
//         // Fetch all the forms we want to apply custom Bootstrap validation styles to
//         var forms = document.getElementsByClassName('needs-validation');
//         // Loop over them and prevent submission
//         var validation = Array.prototype.filter.call(forms, function(form) {
//             form.addEventListener('click', function(event) {
                
//                 if (form.checkValidity() === false) {
//                     event.preventDefault();
//                     event.stopPropagation();
//                 }
//                 form.classList.add('was-validated');
//             }, false);
//         });
//         if(validation == true){
//             console.log("false");
//             var frm = new FormData(document.getElementById("orderForms")); 
//             frm.forEach(element => {
//                 console.log(element);
//             });
//         }
        
//     }, false);
//     
// })();


// previous date disabled
function SetMinDate() {
    var now = new Date();

    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);

    var today = now.getFullYear() + "-" + (month) + "-" + (day);

    $('#inputDeliveryDate').val(today);
    $('#inputDeliveryDate').attr('min', today); 
}

SetMinDate();


var lclCheck = localStorage.getItem('CART');
var cart = lclCheck ? JSON.parse(lclCheck) : [];

function changeNumberOfUnits(proudct_id, action) {
    cart.forEach((element, index) => {
        if (element.product_id == proudct_id) {
            if (action == "plus") {
                element.quntity += 1;
            }
            else if (action == "minus" && element.quntity > 0) {
                element.quntity -= 1;
            }
            // renderCartItem();
            renderCartItem();
            subTotal();
        }
        
    });
    localStorage.setItem('CART', JSON.stringify(cart));
}

function renderCartItem() {
    parentCart.innerHTML = "";
    cart.forEach((element, index) => {
        parentCart.innerHTML += `
        <div class="row">
            <div class="col-3 align-self-center">
                <img src="/media/${element.image}"
                    class="img-fluid rounded-3" style="height: 55px;" alt="">
            </div>
            <div class="col-9 d-flex flex-column ">
                <div class="text-truncate">${element.product_name}</div>
                <div class="row d-flex justify-content-center align-items-center">
                    <div class="col-6 d-flex justify-content-center align-items-center">
                        <button class="minusBtn btn px-2" onclick="changeNumberOfUnits(${element.product_id}, 'minus')">
                            <i class="fas fa-minus"></i>
                        </button>

                        <input id="form${element.product_id}" min="0" name="quantity" value="${element.quntity}" type="number"
                            class="form-control form-control-sm text-center" style="height: fit-content;" />

                        <button class="btn px-2" onclick="changeNumberOfUnits(${element.product_id}, 'plus')">
                            <i class="plusBtn fas fa-plus"></i>
                        </button>
                    </div>
                    <div class="col-3">
                        &#2547;<span id="cartPrdPrice${element.product_id}">${element.quntity * element.price}</span>
                    </div>
                    <div class="col-3">
                        <i class="deleteItem text-danger fas fa-trash fa-lg" onclick="deleteBtn(${index})"></i>
                    </div>
                </div>
            </div>

        </div>
        <hr class="my-4">
        `;
    });

    // document.querySelector(".cart-details").insertAdjacentHTML("beforeend", html);
}


window.addEventListener('DOMContentLoaded', (event) => {
    renderCartItem();
    subTotal();
});


function subTotal(){
    var totalPrice = 0;
    var totalItem = 0;
    cart.forEach((element,index)=>{
        totalPrice += (element.price * element.quntity);
        totalItem += element.quntity;
    })
    
    cartSubtotal.innerText = `${totalPrice} (${totalItem} items)`;
    checkoutPageSubtotal.innerText = `${totalPrice}`;
    
    if(totalPrice>0){
        checkoutPageTotal.innerText = `${totalPrice+50}`;
        shippingPrice.innerText = 50;
    }else{
        checkoutPageTotal.innerText = 0;
        shippingPrice.innerText = 0;
    }


    cartIcon.innerText = totalItem;
    cartIconMb.innerText = totalItem;

}





  