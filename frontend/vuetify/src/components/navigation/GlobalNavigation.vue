<template>
  <v-navigation-drawer
    style="max-height: 50vh;"
    temporary
    dark
    right
    fixed
    width="256px"
    color="primary"
    v-if="$store.state.globalDrawer"
    v-model="$store.state.globalDrawer"
    :key="loggedIn"
  >

  <v-btn
    icon
    absolute
    right
    color="blood"
    @click="drawer = false"
  >
    <v-icon>close</v-icon>
  </v-btn>
  <v-container class="pa-5">
    <v-layout 
      column 
      align-center 
      justify-center
    >

      <div v-if="!user">
        <h2 class="title">User Settings</h2>
      </div>

      <div v-else>
          <h2 class="title">{{ user.name }}</h2>
          <p class="body-2 text-center">{{ user.email }}</p>
          <div v-if="user.profile.ImgUrl==='none' || ''">
            <v-avatar class="ma-4" size="80">
            <img :src="images.blankProfile"/>
          </v-avatar>
        </div>
        <div v-else>
          <v-avatar class="ma-4" size="80">
            <img :src="user.profile.ImgUrl" />
          </v-avatar>
        </div>
      </div>

         </v-layout>
  </v-container>

  <!-- User is authenticated -->
    <v-list dense nav>
      <!-- <v-subheader>Account</v-subheader> -->
      <v-list-item-group
        color="primary"
        v-if="user"
      >
        <v-list-item
          @click="changeDashboardComponent(link.dashboardComponent)"
          v-for="(link, i) in accountLinks"
          :key="i"
          :color="activeLinkColor"
          :to="link.target"
        >
          <v-list-item-icon :color="activeLinkColor">
            <v-icon v-text="link.icon"></v-icon>
          </v-list-item-icon>
            <v-list-item-title v-text="link.text"></v-list-item-title>
        </v-list-item>
      </v-list-item-group>

      <!-- User is NOT authenticated -->
    <v-list-item-group
      color="primary"
      v-else
    >
        <v-list-item
          @click="$eventHub.$emit('registration')"
          :color="activeLinkColor"
        >
          <v-list-item-icon color="primary">
            <v-icon>mdi-shield-account</v-icon>
          </v-list-item-icon>
            <v-list-item-title>Sign In</v-list-item-title>
        </v-list-item>
      </v-list-item-group>

      <!-- <v-subheader>Quick Links</v-subheader> -->
      <v-list-item-group 
        color="primary"
      >
        <v-list-item
          v-for="(link, i) in quickLinks"
          :key="i"
          :color="activeLinkColor"
          :href="link.target"
          :to=link.route
          :target="link.external ? '_blank' : ''"
        >
          <v-list-item-icon color="primary">
            <v-icon v-text="link.icon"></v-icon>
          </v-list-item-icon>
            <v-list-item-title v-text="link.text"></v-list-item-title>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import genericProfileImage from '@/assets/pageimages/Generic-profile-picture.jpg'

export default {
  data() {
    return {
      activeLinkColor: "#fff",
      accountLinks: [{
          "icon": "mdi-shield-account",
          "dashboardComponent": "Account",
          "text": "My Account",
        },
        {
          "icon": "mdi-tools",
          "dashboardComponent": "Feedback",
          "text": "Give Feedback"
        },
        {
          "icon": "mdi-credit-card",
          "dashboardComponent": "Settings",
          "text": "Settings and Privacy"
        },
        {
          "icon": "mdi-credit-card",
          "dashboardComponent": "Support",
          "text": "Help and Support",
        },
        {
          "icon": "mdi-bug",
          "dashboardComponent": "Display",
          "text": "Display and Accessibility"
        },
        {
          "icon": "mdi-logout",
          "dashboardComponent": "logout",
          "text": "Logout"
        }
      ],
      quickLinks: [
        /*  {
            "icon": "mdi-gift",
            "click": "",
            "text": "Gift a Streamer"
          },
          {
            "icon": "mdi-mail",
            "click": "",
            "text": "Contact Us"
          },*/
        /* {
          "icon": "mdi-diamond-stone",
          "target": "/founders-program",
          "text": "Become a Founder",
        },
        {
          "icon": "mdi-library-video",
          "click": "",
          "text": "Our Streamers"
        }, */
        /* {
          "icon": "mdi-discord",
          "target": "https://discord.gg/JUrAdzu",
          "text": "Discord",
          "external": true
        },
        {
          "icon": "mdi-twitter",
          "target": "https://twitter.com/streambeacontv/",
          "text": "Twitter",
          "external": true
        }
      ],
      legalLinks: [
        {
          "icon": "mdi-shield-check",
          "target": "/terms-of-service",
          "text": "Terms of Service"
        },
        {
          "icon": "mdi-shield-lock",
          "target": "/privacy-policy",
          "text": "Privacy Policy"
        },
        {
          "icon": "mdi-help",
          "target": "/faq",
          "text": "FAQ"
        } */
      ], 
      images: {
        blankProfile: genericProfileImage
      },
    };
  },
  methods: {
    changeDashboardComponent(targetComponent) {
      if(targetComponent==="logout") {
        this.drawerLogout()
      }
      
      if (this.$route.name != 'dashboard') {
        this.$router.replace('dashboard')
          .then(() => {
            this.emitter.emit('changeDashboardComponent', targetComponent)
            this.$store.commit('updateDrawer', false)
          })
      } else {
        this.emitter.emit('changeDashboardComponent', targetComponent)
        this.$store.commit('updateDrawer', false)
      }
    },
    drawerLogout() {
      this.$store.commit('updateDrawer', false)
      this.$router.push("/logout")
    }
  },
  computed: {
    loggedIn: {
      get() {
        return this.$store.state.isLoggedIn
      },
      set(value) {
        this.$store.commit('updateLoggedInState', value)
      }
    },
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
      }
    },
    drawer: {
      get() {
        return this.$store.state.globalDrawer
      },
      set(val) {
        return this.$store.commit('updateDrawer', val)
      }
    }
  }
}
</script>
