
*************
API Reference
*************

.. raw:: html

   <style>
     .sphinxsidebar, body {
     background: white;
     }
   
      div[aria-label^=breadcrumbs], footer, #api-reference h1 {
         display: none;
      }
      div.wy-nav-content {
          padding: 0px 0px 0px 0px;
      }
      div.iapiref {
          position: relative;
      }
      iframe.iapiref  {
          position: absolute;
          top: 0;
          width: 100%;
      }
   </style>

   <script>
      /*
            document.getElementById("glu").style.height = document.body.scrollHeight+"px";
      */
      var others=50;
      document.body.onload = function(o){
         document.getElementById("glu").style.height = window.parent.innerHeight-others+"px";
      }
      document.body.onresize = function(o){
         document.getElementById("glu").style.height = window.parent.innerHeight-others+"px";
      }
   </script>  
   
   <div class="iapiref">
      <iframe id='glu'
         class="iapiref"
         src="apiref/index.html"
         allowfullscreen
      ></iframe>
   </div>
