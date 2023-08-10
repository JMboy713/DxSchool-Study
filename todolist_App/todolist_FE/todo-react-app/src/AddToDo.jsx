import React from "react";
import { TextField,Paper,Button,Grid } from "@material-ui/core";

class AddToDo extends React.Component{
	constructor(props){
		super(props);
		// 입력받은 내용을 저장할 state 를 생성한다.
		this.state={item:{title:""}}
		// 넘겨준 데이터를 변수에 대입
		this.add=props.add;
		
	}

	// 입력 내용이 변경될 때 title 을 수정하는 메서드
	onInputChange=(e)=>{
		// item 속성을 복제
		const thisItem=this.state.item;
		// 복제된 객체의 title 의 값을 입력한 내용으로 수정
		thisItem.title=e.target.value;
		// 복제된 객체를 다시 item 으로 복사
		this.setState({item:thisItem});
	}
	// +버튼을 누를 때 호출되는 메서드
	onButtonClick=(e)=>{
		this.add(this.state.item);
		// title 을 clear - 입력상자도 clear 된다.
		this.setState({item:{title:""}})
	}
	// enter 를 눌렀을때 호출되는 메서드
	enterKeyEnterHandler=(e)=>{
		if (e.key==="Enter"){// enter 눌렀을떄 +버튼 누르는 함수와 동일하게 적용
			this.onButtonClick();
		}
	}
	




	render(){
		return(
			<Paper style={{margin:16,padding:16}}>
				<Grid container>
					{/* 11/16의 사이즈로 만든다.  */}
					<Grid xs={11} md={11} item style={{padding:16}}>
						<TextField placeholder="제목을 입력"
						fullWidth
						value={this.state.item.title}
						onChange={this.onInputChange}
						onKeyPress={this.enterKeyEnterHandler}
						/>
					</Grid>
					<Grid xs={1} md={1} item>
						<Button
						fullWidth
						color="secondary"
						variant="outlined"
						onClick={this.onButtonClick}>
							ADD
						</Button>
					</Grid>
				</Grid>
			</Paper>

			)}
	
}export default AddToDo;