export default {

  data() {
    return {
      isMenuOpen: false
    }
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    }
  },
  mounted() {
    window.addEventListener('scroll', () => {
      const nav = this.$el.querySelector('nav');
      if (window.scrollY > 50) {
        nav.classList.add('scroll');
      } else {
        nav.classList.remove('scroll');
      }
    });

    const navLinks = this.$el.querySelectorAll('nav a');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        this.closeMenu();
      });
    });
  }
}
