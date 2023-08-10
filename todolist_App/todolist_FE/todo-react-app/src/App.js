import './App.css';
import React from 'react';
import ToDo from './ToDo';
import {Paper,List, Container} from "@material-ui/core"
import AddToDo from './AddToDo'; // AddToDo 에서 export 한걸 AddToDo 라는 이름으로 불러오겠다. 
import { call } from './service/ApiService';



class App extends React.Component{
  constructor(props){
    super(props)
    this.state={items:[]};
  }
  // 컴포넌트가 메모리 할당을 한 후 출력하기전에 호출되는 메서드
  componentDidMount(){
    // 데이터를 가져오는 API 요청 수행
    call("/main/todo","GET",null).then((response)=>this.setState({items:response.list}))



    // console.log("컴포넌트가 메모리 할당을 받음")
    // // FetchAPI 로 받아오기
    // // 요청 옵션을 생성
    // const requestoptions={
    //   method:"GET",
    //   headers:{"content-Type":"application.json"}
    // };
    // fetch("http://127.0.0.1:8000/main/todo",requestoptions)
    // .then((response)=>response.json())
    // .then((response)=>{
    //   this.setState({items:response.list})
    // },
    // (error)=>{
    //   console.log(error)
    // })
      
    }
  

  // 데이터 추가를 위한 함수
  // Item 1개를 받아서 items 에 추가하는 함수
  add=(item)=>{
    item.userid="jason";
    call("/main/todo","POST",item)
    .then((response)=>this.setState({items:response.list}))


    // const thisItems=this.state.items; // 기존 items를 thisitems에 복제
    // // 추가할 데이터 생성
    // item.id="ID-"+thisItems.length; 
    // item.done=false;
    // // 복제본에 추가. => react 에서는 원본 데이터에 값을 추가할 수 없기 때문에 복제해서 넣는다. 
    // thisItems.push(item);
    // // items에 복제본을 추가. 
    // // react 는 props 나 state 가 변경되면 자동으로 재출력해준다. 
    // this.setState({items:thisItems});
  }
  delete=(item)=>{
    item.userid="jason";
    call("/main/todo","DELETE",item)
    .then((response)=>this.setState({items:response.list}))


    // const thisItems=this.state.items;
    // // thisItems 에서 item 삭제하기 - id가 구별하는 속성
    // const newItems=thisItems.filter((e)=>e.id!==item.id)
    // // state를 변경해서 데이터를 재출력해본다. 
    // this.setState({items:newItems},()=>{
    //   console.log(item.id+"가 제거되었습니다.")
    // })
  }
  update=(item)=>{
    item.userid="jason"
    call("/main/todo","PUT",item)
    .then((response)=> this.setState({items:response.list}))
  }



  render(){
    // map: 데이터의 모임을 순회하면서 함수를 적용해 함수의 리턴 값을 가지고 데이터의 모임을 만들어주는 함수
    // 데이터 변환에 활용
    // 데이터 개수에 따라 다르게 반응하도록 작성. 
    var todoItems=this.state.items.length > 0 &&(
      <Paper style={{margin:16}}>
<List>
  {this.state.items.map((item,idx)=>(
    <ToDo item={item} key={item.id} delete={this.delete} update={this.update}/>
    ))}
</List>

      </Paper>

    )


    return (
      <div className="App">
        <Container maxWidth="md">
        <AddToDo add={this.add} />
        {todoItems} 
        </Container>
        </div>// props 의 이름.
    )
  }
}

export default App;
