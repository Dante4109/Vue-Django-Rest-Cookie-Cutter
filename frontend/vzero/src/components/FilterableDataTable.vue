<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Card Data Table</h1>
    
    <!-- Search and Filter Controls -->
    <div class="mb-6 flex flex-wrap gap-4">
      <div class="flex-grow">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="text-black w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div class="relative">
        <button
          @click="toggleDropdown"
          class="text-black px-4 py-2 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          {{ selectedField || 'Select Field' }}
        </button>
        <div
          v-if="isDropdownOpen"
          class="text-black absolute z-10 mt-1 w-48 bg-white border border-gray-300 rounded-md shadow-lg"
        >
          <div class="p-2">
            <label v-for="field in fields" :key="field" class="flex items-center">
              <input
                type="radio"
                :value="field"
                v-model="selectedField"
                class="mr-2"
                @change="updateFilterOptions"
              />
              {{ field }}
            </label>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Filter Checkboxes -->
    <div v-if="selectedField" class="mb-6">
      <h2 class="text-black text-lg font-semibold mb-2">Filter by {{ selectedField }}:</h2>
      <div class="flex flex-wrap gap-4">
        <label v-for="option in filterOptions" :key="option" class="flex items-center">
          <input
            type="checkbox"
            :value="option"
            v-model="selectedFilters"
            class="mr-2"
          />
          {{ option }}
        </label>
      </div>
    </div>
    
    <!-- Data Table -->
    <table class="w-full border-collapse border border-gray-300">
      <thead>
        <tr class="bg-gray-100">
          <th
            v-for="field in fields"
            :key="field"
            @click="sortBy(field)"
            class="p-2 text-left text-black cursor-pointer hover:bg-gray-200"
          >
            {{ field }}
            <span v-if="sortField === field">{{ sortOrder === 'asc' ? '▲' : '▼' }}</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="card in filteredAndSortedData" :key="card.id" class="border-t border-gray-300 hover:bg-gray-50">
          <td v-for="field in fields" :key="field" class="p-2">
            {{ card[field.toLowerCase()] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Sample data
const cards = ref([
  { id: 1, name: 'Dragon', rarity: 'Rare', power: 5, toughness: 5 },
  { id: 2, name: 'Goblin', rarity: 'Common', power: 2, toughness: 1 },
  { id: 3, name: 'Angel', rarity: 'Uncommon', power: 4, toughness: 4 },
  { id: 4, name: 'Zombie', rarity: 'Common', power: 2, toughness: 2 },
  { id: 5, name: 'Elemental', rarity: 'Uncommon', power: 3, toughness: 3 },
])

const fields = ['Name', 'Rarity', 'Power', 'Toughness']

const searchQuery = ref('')
const selectedField = ref('')
const selectedFilters = ref([])
const sortField = ref('name')
const sortOrder = ref('asc')
const isDropdownOpen = ref(false)
const filterOptions = ref([])

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const updateFilterOptions = () => {
  const field = selectedField.value.toLowerCase()
  filterOptions.value = [...new Set(cards.value.map(card => String(card[field])))]
  selectedFilters.value = []
}

const sortBy = (field) => {
  const lowerField = field.toLowerCase()
  if (sortField.value === lowerField) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortField.value = lowerField
    sortOrder.value = 'asc'
  }
} 

const filteredAndSortedData = computed(() => {
  let result = cards.value

  // Apply search filter
  if (searchQuery.value && selectedField.value) {
    const query = searchQuery.value.toLowerCase()
    const field = selectedField.value.toLowerCase()
    result = result.filter(card => String(card[field]).toLowerCase().includes(query))
  }

  // Apply checkbox filters
  if (selectedFilters.value.length > 0 && selectedField.value) {
    const field = selectedField.value.toLowerCase()
    result = result.filter(card => selectedFilters.value.includes(String(card[field])))
  }

  // Apply sorting
  result.sort((a, b) => {
    let comparison = 0
    if (a[sortField.value] > b[sortField.value]) comparison = 1
    if (a[sortField.value] < b[sortField.value]) comparison = -1
    return sortOrder.value === 'desc' ? comparison * -1 : comparison
  })

  return result
})
</script>