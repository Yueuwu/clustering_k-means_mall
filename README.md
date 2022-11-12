<h1 align="center">Data clustering by k-means method based on data about mall customers!</h1>
<h3>Description: </h3> <p>This is another assignment in AI course in university.
This program clustering customers by two indications: Annual Income and Spending Score.</p>
<h2>Technologies: </h2>
<ul>
    <li style="font-size: 18px;">Python 3.10</li>
    <li style="font-size: 18px;">Pandas</li>
    <li style="font-size: 18px;">Scikit-learn</li>
    <li style="font-size: 18px;">Matplotlib</li>
</ul>
<h2>How it works?</h2>
<p>First of all we need to drop useless information for our journey such as id, gender, age.</p>
<p>Next step will be boring transformation of info and standardization.</p>
<p>After that we use elbow method. With this method we find out how many clusters this data contains.</p>
<div align="center"><img width="400" height="350" src=".\img\Elbow method.png"/></div>
<p>As we see the WCSS (within-cluster sum of squares) value starts to decrease more slowly from 5 clusters.</p>
<p>So it means that we take this value as number of clusters.</p>
<p>Since we know count of clusters and necessary information, we can try figure clusters out and display it!</p>
<div align="center"><img src=".\img\clustering done.png" width="400" height="350"/></div>