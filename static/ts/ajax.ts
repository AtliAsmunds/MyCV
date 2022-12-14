
let nrOfParticipants = 1;

jQuery(() => {
  armPage('about');
  armPage('work');
  armPage('education');
  armPage('skills');
  armPage('music');
  armPage('email');

  setStars();
  addPraticipant();
  removeParticipant();


  $('textarea').on('input', function () {
    // debugger;
    $(this).height("");
    const scrollHeight = $(this).prop('scrollHeight');
    $(this).height(scrollHeight);

  })


  $('.nav-item').on('click', handleMenu)
  $('.hamburger').on('click', handleMenu)


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
  const titles = {
    about: 'Um Mig',
    work: 'Reynsla',
    education: 'Menntun',
    skills: 'Hæfni',
    music: 'Tónlist',
    email: 'Hafa Samband',
  }
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
    type TitleKey = keyof typeof titles;
    const key = elemId as TitleKey

    $('title').html(titles[key])
    $(".grid-container").html(data);
    $("html").animate({
      scrollTop: 0
    }, 1000)
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

function addPraticipant(){
  $('#add-name').on("click", () => {
    nrOfParticipants++;

    const inputList = $('.name-inputs')
    
    const inputDiv = $('<div>')
    const nameInput = $('<input>');
    const mailInput = $('<input>');

    nameInput.attr({
      type: 'text',
      id: `name${nrOfParticipants}`,
      name: `name${nrOfParticipants}`,
      placeholder: `Nafn ${nrOfParticipants}`
    });

    mailInput.attr({
      type: 'email',
      id: `mail${nrOfParticipants}`,
      name: `mail${nrOfParticipants}`,
      placeholder: `Email ${nrOfParticipants}`
    });

    // inputDiv.append(newLabel, $('<br>'), newInput, $('<br>'));
    inputDiv.append(nameInput, mailInput, $('<br>'));
    inputList.append(inputDiv);

    $('#remove-name').prop('disabled', false);
  })
}

function removeParticipant(){
  $('#remove-name').on("click", () => {
    if (nrOfParticipants > 1) {
      $('.name-inputs').children().last().remove();

      nrOfParticipants--;

      if (nrOfParticipants <= 1) {
        $('#remove-name').prop('disabled', true)
      }
    }
  })
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


function handleMenu() {
  const nav = $('nav');

  if (nav.hasClass('showMenu')) {
    nav.removeClass('showMenu');
    $('.closeIcon').css('display', 'none');
    $('.menuIcon').css('display', 'block');
  } else {
    nav.addClass('showMenu');
    $('.closeIcon').css('display', 'block');
    $('.menuIcon').css('display', 'none');

  }
}