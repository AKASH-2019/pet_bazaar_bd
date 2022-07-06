console.log("i am");

// document.getElementById("emailSend").addEventListener("click",async ()=>{
//     console.log("from email");
//     var data = await fetch("/ordeEmail",{
//         method: 'post',
//         // body: frm
//     });

//     var res = await data.json();
//     console.log("res");

// });

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
            renderCartItem();
            // renderCartPage();
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
                        <i class="deleteItem text-danger fas fa-trash fa-lg cursor-pointer" onclick="deleteBtn(${index})"></i>
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


function deleteBtn(index){
    var storage = window.localStorage;
    storage.clear();
    cart.splice(index, 1);
    storage.setItem("CART", JSON.stringify(cart));

    renderCartItem();
    subTotal();
    
}

// document.querySelectorAll(".item-a").forEach(el =>{
//     console.log("dddd")
//     el.style.width = "280px";
// })

document.querySelectorAll(".cart-btn").forEach(el => {

    el.addEventListener("click", (e) => {
        e.preventDefault();
        var price = e.target.getAttribute("data-price");
        var name = e.target.getAttribute("data-name");
        var slug = e.target.getAttribute("data-slug");
        var product_id = e.target.getAttribute("data-id");
        var img = e.target.getAttribute("data-img");
      

        var ob = {
            "order_details_id": 0,
            "product_id": product_id,
            "product_name": name,
            "price": price,
            "slug": slug,
            "image": img,
            "quntity": 1
        };

        e.target.childNodes[1].classList.remove("d-none");
        e.target.setAttribute("disabled", true);

        setTimeout(() => {
            e.target.childNodes[1].classList.add("d-none");
            e.target.removeAttribute("disabled");
            subTotal();
        }, 3000);

        if (cart != null && cart.some(item => item.product_id == product_id)) {
            changeNumberOfUnits(product_id, "plus");
        } else {
            cart.push(ob);
            renderCartItem();
        }

        localStorage.setItem('CART', JSON.stringify(cart));

    })
})


function subTotal(){
    var totalPrice = 0;
    var totalItem = 0;

    cart.forEach((element,index)=>{
        totalPrice += (element.price * element.quntity);
        totalItem += element.quntity;
    })
    
    // cartSubtotal.innerHTML = `<p>Subtotal: &#2547;${totalPrice} (${totalItem} items)</p>`;
    cartSubtotal.innerText = `${totalPrice} (${totalItem} items)`;

    
    cartIcon.innerText = totalItem;
    cartIconMb.innerText = totalItem;
    
}











