const app = new Vue({
    delimiters: ['${', '}$'],
    el:'#app',
    data: {
        
        titulo: 'GYM con Vue',
        tareas: [],
        nuevaTarea: '',
        suma: 0,
        guardar:false
        
    },
    methods:{
        agregarTarea: function(){
            this.tareas.push({
                nombre: this.nuevaTarea,
                estado: false,
                
            
            });
            console.log(this.tareas); 
            this.nuevaTarea= '';
            this.sumarTarea();//
            
        },
        editarTarea: function(index){
            this.tareas[index].estado = true;
        },
        eliminarTarea: function(index){
            this.tareas.splice(index, 1);
            this.sumarTarea();
        },
        sumarTarea: function(){
            var sumatoria=0;
            for (var i = 0; i < this.tareas.length; i++)
                {
                    //console.log(this.tareas[i]);
                    sumatoria += parseInt(this.tareas[i].nombre);
                }
            this.suma = sumatoria;    
            console.log(sumatoria);
            if (this.suma>0){
                this.guardar = true;

            }
            else{
                this.guardar = false;
            }
            }

    }
});