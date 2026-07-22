#contacts/views.py
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import ContactMessage


class ContactView(CreateView):

    model = ContactMessage

    form_class = ContactForm

    template_name = 'contacts/tel.html'

    success_url = reverse_lazy('contacts:contacts')

    def form_valid(self, form):

        obj = form.save()

        send_mail(
            subject=obj.subject,

            message=f'''
Имя: {obj.name}

Email: {obj.email}

Сообщение:

{obj.message}
''',

            from_email=None,

            recipient_list=[
                'admin@intershop.ru'
            ],

            fail_silently=False,
        )

        messages.success(
            self.request,
            'Спасибо! Сообщение отправлено.'
        )

        return super().form_valid(form)
