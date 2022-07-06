console.log("i am from admin order list");

// // var cart = [];
// var lclCheck = localStorage.getItem('CART');


async function statusUpdate(order_id) {
    var statusSelect = document.getElementById(`orderStatusSelectData${order_id}`);
    // var selectedText = ddlFruits.options[ddlFruits.selectedIndex].innerHTML;
    var selectedValue = statusSelect.value;
    if(selectedValue != 0){
        // alert("order id: "+ order_id + " Value: " + selectedValue);
        var frm = new FormData(document.getElementById(`orderStatusForm${order_id}`));
        frm.append("order_id",order_id); 

        // frm.forEach(element => {
        //     console.log(element);
        // });

        var data = await fetch('/pet/admin/order/status/update',{
            method: 'post',
            body: frm
        });

        // var res = await data.json();
        // console.log(res);
    }
}



















