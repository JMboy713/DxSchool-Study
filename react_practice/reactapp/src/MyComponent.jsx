import React,{Component} from "react";

class MyComponent extends Component{
	render(){
		return(
			<div>두산의 첫번쨰 우승은 {this.props.team}</div>
		)
	}
}

export default MyComponent;