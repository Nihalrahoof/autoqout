// Define your API here
var productListApiUrl = 'https://web-production-04f73.up.railway.app/getProducts';
var uomListApiUrl = 'https://web-production-04f73.up.railway.app/getUOM';
var productSaveApiUrl = 'https://web-production-04f73.up.railway.app/insertProduct';
var productDeleteApiUrl = 'https://web-production-04f73.up.railway.app/deleteProduct';
var customerSaveApiUrl = 'https://web-production-04f73.up.railway.app/insertCustomers';
var quotationSaveApiUrl = 'https://web-production-04f73.up.railway.app/insertQuotations';
var customerTotalsApiUrl = 'https://web-production-04f73.up.railway.app/getCustomers';
var quotationListApiUrl = 'https://web-production-04f73.up.railway.app/getlists';
var quotationDeleteApiUrl = 'https://web-production-04f73.up.railway.app/deleteQuotation';

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
