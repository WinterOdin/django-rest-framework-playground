listBuilder()
function listBuilder(){
    var wrapper = document.getElementsByClassName('listWrapper')
    var url     = 'http://127.0.0.1:8000/api/taskList/'

    fetch(url)
    .then((resp) => resp.json)
    .then(function(data){
        console.log('Data',data)
        var list = data
        for (var i in list){
            
            var item = `
                <div id="data-row-${i}" class="taskWrapper flexWrapper">
                
                    <div style="flex:7">
                        <span class="title">${list[i].title}</span>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-info edit">Edit</button>
                    </div>
                    <div style="flex:1">
                    <button class="btn btn-sm btn-outline-dark delete">Delete</button>
                    </div>                
                </div>
            `
            wrapper.innerHTML += item
        }
    })
}