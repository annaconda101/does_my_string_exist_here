from django.shortcuts import render, redirect

from forms import FindTextForm


def index(request):

    if request.method == 'POST':
        form = FindTextForm(data=request.POST)
        if form.is_valid():
            text_to_search = form.data['text_to_search']
            subtext = form.data['subtext']

            result = get_result(text_to_search, subtext)

            context = {
                'form': form,
                'result': result,
                'previous_text_to_search': text_to_search,
                'previous_subtext': subtext

            }

            return render(request, 'index.html', context)

    else:
        form = FindTextForm()
        result = None
        text_to_search = None
        subtext = None

        context = {
            'form': form,
            'result': result,
            'previous_text_to_search': text_to_search,
            'previous_subtext': subtext

        }

        return render(request, 'index.html', context)


def get_result(text_to_search, subtext):
    text_to_search = text_to_search.lower()
    subtext = subtext.lower()

    occurrences = [index + 1 for index in range(len(text_to_search)) if text_to_search.startswith(subtext, index)]

    return tuple(occurrences)
