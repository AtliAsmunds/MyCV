const navHeight = $('nav').outerHeight();
const footerHeight = $('footer').outerHeight();
const minHeight = `calc(100vh - ${navHeight + footerHeight}px)`;
$('.grid-wrapper').css("min-height", minHeight)

jQuery(() => {

  armPage('about');
  armPage('work');
  armPage('education');
  armPage('skills');

  setStars();


  window.onpopstate = () => {
    // debugger;
    let id = window.location.pathname;
    if (id === '/') {
      id = 'about';
    } else {
      id = id.replace(/\//g, '');
    }
    renderPage(id, true);
  }

})

async function renderPage(elemId: string, back = false) {
  let data;
  const url = `/${elemId}-tag/`
  try {
    const response = await fetch(url)

    if (!response.ok) {
      throw new Error("Result not ok");
    }
    data = await response.text();
  } catch (e) {
    console.warn('Unable to fetch data', e)
    data = null;
  }
  if (data) {
    $(".grid-container").html(data);
    if (!back) window.history.pushState('', '', `/${elemId}/`)
    if (elemId == 'skills') setStars();
  }
}

function armPage(elemId: string) {
  const elem = $(`#${elemId}`);

  elem.on("click", () => {
    renderPage(elemId);
  });
}

function setStars() {
  $('.stars').each(function () {
    const level = Number($(this).attr('level'));
    let index = 0;

    $(this).children().each(function() {
      if (index < level) {
        // debugger;
        $(this).removeClass('star-empty');
        $(this).addClass('star-full');
        index++;
      }
    })
  })
}