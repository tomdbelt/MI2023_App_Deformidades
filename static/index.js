$( document ).ready(function(){
    $('input[name=r_fruit]').on('change', function() {
        var n = $(this).val();
        switch(n) {
            case 'manzana':
                $('#imgs_reference').html(
                    `<div class="grid grid-flow-col content-center items-center border-right"> 
                        <img src="./static/imgs/manz-extra.jpg" alt="ref-manzana" class="img"/>
                        <p class="text-center">Extra</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center"> 
                        <img src="./static/imgs/manz-1.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 1</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center border-left"> 
                        <img src="./static/imgs/manz-2.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 2</p>
                    </div>`
                );

                $('#info_models').html(
                    `<div class="grid grid-cols-3 gap-4"> 
                        <div class="block">
                            <p><b>Nombre:</b> MobileNetV2</p>
                        </div>
                        <div class="block">
                            <p><b>Learning Rate:</b> 0.001</p>
                        </div>
                        <div class="block">
                            <p><b>Batch Size:</b> 32</p>
                        </div>
                        <div class="block">
                            <p><b>Épocas:</b> 11</p>
                        </div>
                        <div class="block">
                            <p><b>Dropout:</b> 0.3</p>
                        </div>
                    </div>`
                );
                break;

            case 'mango':
                $('#imgs_reference').html(
                    `<div class="grid grid-flow-col content-center items-center border-right">
                        <img src="./static/imgs/mango-extra.jpeg" alt="ref-manzana" class="img"/>                
                        <p class="text-center">Extra</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center"> 
                        <img src="./static/imgs/mango-1.jpeg" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 1</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center border-left"> 
                        <img src="./static/imgs/mango-2.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 2</p>
                    </div>`
                );

                $('#info_models').html(
                    `<div class="grid grid-cols-3 gap-4"> 
                        <div class="block">
                            <p><b>Nombre:</b> MobileNetV2</p>
                        </div>
                        <div class="block">
                            <p><b>Learning Rate:</b> 0.001</p>
                        </div>
                        <div class="block">
                            <p><b>Batch Size:</b> 32</p>
                        </div>
                        <div class="block">
                            <p><b>Épocas:</b> 30</p>
                        </div>
                        <div class="block">
                            <p><b>Dropout:</b> 0.3</p>
                        </div>
                    </div>`
                );
                break;

            case 'fresa':
                $('#imgs_reference').html(
                    `<div class="grid grid-flow-col content-center items-center border-right"> 
                        <img src="./static/imgs/fresa-extra.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Extra</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center"> 
                        <img src="./static/imgs/fresa-1.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 1</p>
                    </div>
                    <div class="grid grid-flow-col content-center items-center border-left"> 
                        <img src="./static/imgs/fresa-2.png" alt="ref-manzana" class="img"/>
                        <p class="text-center">Clase 2</p>
                    </div>`
                );

                $('#info_models').html(
                    `<div class="grid grid-cols-3 gap-4"> 
                        <div class="block">
                            <p><b>Nombre:</b> MobileNetV2</p>
                        </div>
                        <div class="block">
                            <p><b>Learning Rate:</b> 0.001</p>
                        </div>
                        <div class="block">
                            <p><b>Batch Size:</b> 32</p>
                        </div>
                        <div class="block">
                            <p><b>Épocas:</b> 23</p>
                        </div> 
                        <div class="block">
                            <p><b>Dropout:</b> 0.3</p>
                        </div>
                    </div>`
                );
                break;
        }
    });
});

$( window ).on( "load", function() {
    $('#r_manzana').trigger( "change" );
});