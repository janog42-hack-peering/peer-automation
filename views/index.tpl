%include('header.tpl', title='TopPage')
<main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
    <span style="font-size:40px">Automation</span>
  <form action="/auto" method="POST">
  <div class="form-group">
    <label for="TARGET">TARGET</label>
    <input type="text" class="form-control" name="TARGET" id="TARGET" placeholder="TARGET">
  </div>
  <div class="form-group">
    <label for="ASN">ASN</label>
    <input type="text" class="form-control" name="ASN" id="ASN" placeholder="ASN">
  </div>
  <div class="form-group">
    <label for="IXID">IX</label>
    <select class="form-control" name="IXID" id="IXID">
        <option value=145>JPNAPOS</option>
        <option value=564>JPIXOS</option>
        <option value=95>JPNAPTY</option>
        <option value=30>JPIXTY</option>
    </select>
  </div>
  <div class="form-group">
    <label for="Password">Password</label>
    <input type="text" class="form-control" id="PASSWORD" name="PASSWORD" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="In-Policy">In-Policy</label>
    <input type="text" class="form-control" id="INPOLICY" name="INPOLICY" placeholder="In-Policy">
  </div>
  <div class="form-group">
    <label for="In-Policy">Ipv4 / Ipv6</label>
    <select class="form-control" id="IPV" name="IPV">
        <option value=4>Ipv4</option>
        <option value=6>Ipv6</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

<pre>
{{result}}
</pre>


</main>
</div>
</div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js"></script>

    <!-- Icons -->
    <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace()
    </script>
     <script>
      $(document).ready(function() {
          $('#btn_insert').click(function() {
                $('#form_issue').submit();
         });

        });
    </script>

  </body>
</html>
