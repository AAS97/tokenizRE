<template>
  <div
    id="card"
    class="bg-white bg-opacity-40 rounded-md my-4 w-5/12 flex flex-col items-center justify-center px-4 border-2 border-white border-opacity-20 border-solide"
    style="backdrop-filter: blur(10px);"
  >
    <div class="text-center mt-4">
      <h1 class="text-2xl py-5 text-gray-900">Tokenize</h1>
      <p id="description" class="text-l pb-5 text-gray-800">
        Enter all the info about the property
      </p>

      <form
        action=""
        class="bg-white bg-opacity-30 rounded-md px-8 pt-6 pb-8 space-y-5 mb-4 border-2 border-white border-opacity-20 border-solide"
        style="backdrop-filter: blur(10px);"
      >
        <input
          v-model="property_name"
          placeholder="Property name"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        />
        <select
          v-model="property_type"
          placeholder="What type of property"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        >
          <!-- <option disabled value="">What type of property</option> -->
          <option>Appartment</option>
          <option>House</option>
          <option>Residential Building</option>
          <option>Office Building</option>
          <option>Venue</option>
        </select>
        <input
          v-model="property_address"
          placeholder="Property address"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        />
        <input
          v-model="surface"
          type="number"
          placeholder="Surface (m2)"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        />
        <textarea
          v-model="property_description"
          placeholder="Property description"
          cols="30"
          rows="10"
          class="bg-gray-100 p-1 appearance-none border rounded w-full text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        ></textarea>
        <a href="#" class="bg-black text-white px-4 py-6 no-underline"
          >Submit property</a
        >
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreationCard",
};
</script>

<style>
/* <div class="w-full md:w-1/2 text-center md:text-right pb-4 md:p-0">
					<input type="search" placeholder="Search..." class="bg-gray-300 border text-sm p-1" />
				</div> */
</style>
