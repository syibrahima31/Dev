const addBtn = document.querySelector('.add-btn')


// 新增按鈕
addBtn.addEventListener('click',(e)=>{
  const inputValue = document.querySelector('input[name=todo]').value;
  
 const todos = document.querySelector('.todos') 
  const todo = document.createElement('LI');
  todo.classList.add('list-group-item','d-flex','justify-content-between','align-items-center');
  todo.innerHTML=`
      
      <div>
          <span class="badge bg-secondary">未完成</span>
          ${inputValue}
      </div>
      <div>
          <button class="btn btn-danger btn-sm delete">刪除</button>
          <button class="btn btn-primary btn-sm change">已完成</button>
      </div>
    `;
    todos.appendChild(todo);
    document.querySelector('input[name=todo]').value="";
})

document.querySelector('.todos').addEventListener('click',function(e){
  //項目  
  const list =e.target.closest('.list-group-item');
  const badge =list.children[0].children[0]
  //變更狀態
  if(e.target.classList.contains('change')){
    if(badge.classList.contains('bg-secondary')){
      badge.innerText="已完成"
      badge.classList.toggle('bg-danger')
      e.target.innerText="未完成"
    }
    if(badge.classList.contains('bg-danger')){
      badge.classList.toggle('bg-secondary')
      badge.innerText="未完成"
      e.target.innerText="已完成"
    }
  }
  //刪除
  if(e.target.classList.contains('delete')){
    document.querySelector('.todos').removeChild(list)
  }
}) 

