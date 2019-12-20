var d = document
var q
var ingredient
var c = 0
function addRow(){
    ingredient = d.getElementById('inputState').value
    q = d.getElementById('inputCity').value

    if(ingredient === ''){
        alert('Выберите ингредиент и укажите количесво!')
    } else if (q === ''){
        alert('Выберите ингредиент и укажите количесво!')
    }
    else{

    c++

    var tbody = d.getElementById('tab').getElementsByTagName('TBODY')[0]

    var row = d.createElement('TR')
    tbody.appendChild(row)

    var td1 = d.createElement('TD')
    var td2 = d.createElement('TD')
    var td3 = d.createElement('TD')

    var delete_name = `delete_${c}`
    var value_name = `value_${c}`
    var name_name = `name_${c}`


    td1.setAttribute('id', name_name)

    var q_input = d.createElement('input')
    q_input.setAttribute('id', value_name)
    q_input.type = 'number'
    q_input.value = q

    var deleteButton = d.createElement('input')
    deleteButton.setAttribute('id', delete_name)
    deleteButton.type = 'submit'
    deleteButton.value = 'delete'
    deleteButton.addEventListener('click', function(){
        var delete_element = this
        var id_name = delete_element.getAttribute('id')
        delButton(id_name);
        return false
    })

    td3.appendChild(deleteButton)
    td2.appendChild(q_input)

    row.appendChild(td1)
    row.appendChild(td2)
    row.appendChild(td3)

    td1.innerHTML = ingredient
    }
}

function delButton(id_name){
    var delete_element = d.getElementById(id_name)
    var ell = delete_element.parentElement.parentElement
    ell.remove()
}

var btn_add_ajax = d.getElementById('btn_ajax')
btn_add_ajax.addEventListener('click', getRecipe)

function getRecipe(){          
    new_component= d.getElementsByTagName('tr')
    var recipe_name = d.getElementById('recipe_name')

    length_list_ingredient = new_component.length
    var respons_dict = new Map()

    if(length_list_ingredient>1){
        for(let i = 1; i<length_list_ingredient; i++){

            var name = new_component[i].children[0].innerHTML
            var value = Number(new_component[i].children[1].children[0].value)

            if(respons_dict.has(name)){
                value = respons_dict.get(name)+value
                respons_dict.set(name, value)
            }else{
            respons_dict.set(name, value)
            }
        }
        $.ajax({
            url: 'search',
            type: 'GET',
            contentType: 'charset=UTF-8',
            data:{
                'selected': JSON.stringify({'value':Array.from(respons_dict.values()),
                                            'name':Array.from(respons_dict.keys())})
            },
            dataType: 'json',
            success: function(data){
                recipe_name.innerHTML = ''
                var respons_data = new Map(Object.entries(data))                       

                if(respons_data.size > 0){
                
                    for(var[key, value] of respons_data){
                        console.log(key+'-'+value)
                        var creat_h3 = d.createElement('h3')
                        creat_h3.innerHTML = key+': '+value+' порц.'
                        recipe_name.append(creat_h3)

                    }
                }else{
                    recipe_name.innerHTML = "Нет подходящих рецептов!"
                }
            },
            statusCode:{
                404: function(){
                    console.log('page not found')
                }
            } 
        })
    }
    else{
        alert('Добавте ингредиенты в таблицу!')
    }
}