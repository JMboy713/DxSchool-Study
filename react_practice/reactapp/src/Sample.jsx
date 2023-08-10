function Sample(props){
	// 자바스크립트의 구조 분해 할당
	const {team,children}=props;
	return(
		<div>라이벌은 {team}
		현재 순위는 {children}</div>
	)
}
export default Sample;