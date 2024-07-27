// Define your api here
var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var customerSaveApiUrl = 'http://127.0.0.1:5000/insertCustomers';
var quotationSaveApiUrl = 'http://127.0.0.1:5000/insertQuotations';
var customerTotalsApiUrl = 'http://127.0.0.1:5000/getCustomers';
var quotationListApiUrl = 'http://127.0.0.1:5000/getlists';
var quotationDeleteApiUrl = 'http://127.0.0.1:5000/deleteQuotation';
// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}


function productParser(product) {
    return {
        id : product.id,
        name : product.employee_name,
        unit : product.employee_name,
        price : product.employee_name
    }
}

function productDropParser(product) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });