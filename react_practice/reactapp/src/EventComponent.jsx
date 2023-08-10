import React, { Component } from "react";

class EventComponent extends Component{
	state={
		content:''
	}
	render(){
		return(
			<div>
				이벤트 연습
				<input type="text"
				onChange={
					(e)=>{console.log(e.target.value);
					this.setState({content:e.target.value})}
				}/>
				
				
			</div>
		)

	}
}
export default EventComponent