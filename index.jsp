<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" isELIgnored="false"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<link href="css/index.css" rel="stylesheet" type="text/css" />
<title>Insert title here</title>

</head>
<body>
<div id=header>
</div>
<div id=shangchuan>
<div id=shangchuan_in>
	<form action="${pageContext.request.contextPath }/Down" method="POST" enctype="multipart/form-data">
		<input type="file" id=file name="csv"/><br>
		<input type="submit" id=submit value="上  传"/>
	</form>
</div>
</div>
<div id=xiazai>
<div id=xiazai_in>
<!-- 遍历Map集合 -->
    <c:forEach var="me" items="${fileNameMap}">
        <c:url value="/Downloadservlet" var="downurl">
             <c:param name="filename" value="${me.key}"></c:param>
       	</c:url>
        ${me.value}<a href="${downurl}">下载</a>
        <br/>
    </c:forEach>
</div>
</div>
	

</body>
</html>