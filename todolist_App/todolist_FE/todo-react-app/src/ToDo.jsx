// React.js 파일에서 export한 객체를 react 로 받아서 사용
// {이름} 의 경우에는 export 한 객체에서 이름에 해당하는것만 받아서 사용
import React from "react";
import {
	ListItem,
	ListItemText,
	InputBase,
	Checkbox,
	ListItemSecondaryAction,
	IconButton
}from "@material-ui/core";

import DeleteOutlined from "@material-ui/icons/DeleteOutlined"// 휴지통 아이콘


class ToDo extends React.Component{
	constructor(props){
		super(props)//상위 컴포넌트로부터 넘겨받은 데이터를 나의 props에 저장. 
		// props는 읽기전용이기 때문에 수정을 하고자 하는 경우 state에 복사해서 사용해야 한다. 
		this.state={item:props.item,readOnly:true} // state.item 으로 명명. 
		this.delete=props.delete;
		this.update=props.update;
		
	}
	// Event 가 발생하면 readOnly 의 값을 False로 수정
	offReadOnlyMode=(e)=>{
		// state의 값을 바로 변경 ( 복사를 하지 않음 )
		this.setState({readOnly:false})
	}

	// Enter를 눌렀을 때 동작하는 메서드
	enterKeyEventHandler=(e)=>{
		if(e.key==="Enter"){
			this.setState({readOnly:true});
			this.update(this.state.item);
		}
	}

	// Input의 내용을 변경했을때 호출메서드
	editEventHandler=(e)=>{
		const thisItem=this.state.item;
		thisItem.title=e.target.value;
		this.setState({item:thisItem});
		this.update(this.state.item);
	}

	// checkbox 눌렀을 때 호출메서드
	checkeboxEventHandler=(e)=>{
		const thisItem=this.state.item;
		thisItem.done=!thisItem.done;
		this.setState({item:thisItem});
		this.update(this.state.item);
	}

	// 삭제 이벤트
	deleteEventHandler=(e)=>{
		this.delete(this.state.item);
	}

	

	render(){
		const item=this.state.item;
		return(
			<ListItem>
				<Checkbox checked={item.done} onChange={this.checkeboxEventHandler}/>
				<ListItemText>
					<InputBase
					inputProps={{"aria-label":"naked",readOnly:this.state.readOnly}}
					type="text"
					id={item.id}
					name={item.id}
					value={item.title}
					multiline={true}
					fullWidth={true}
					onClick={this.offReadOnlyMode}
					onKeyPress={this.enterKeyEventHandler}
					onChange={this.editEventHandler}
					/>
				</ListItemText>
				<ListItemSecondaryAction>
					{/* icon 은 이벤트를 못받기 때문에 버튼으로 감쌌다.  */}
					<IconButton aria-label="Delete-Todo" onClick={this.deleteEventHandler}>
						<DeleteOutlined/> 
					</IconButton>
				</ListItemSecondaryAction>

			</ListItem>
		)
	}
}
export default ToDo;

