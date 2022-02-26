from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'dt_nasc', 'salary', 'bio', 'photo']



"""
<style type="text/css">
        div.bg {
            background-color: #563d7c;
            height: 50px;
            border: 1px solid #fff;
            }
        div.bg1 {
            background-color: #f20000;
            height: 50px;
            border: 1px solid #fff;
            }
    </style>
    
    <div class="row">
              <div class="col-lg-6 col-sm-12">
                  <span>Plataforma de Venda</span> <!- class="text-muted" ->
              </div>
              <div class="col-lg-6 col-sm-12">
                  <a href="https://comunicaria.com/">Comunicaria</a><!- class="text-muted" ->
              </div>
          </div>
"""