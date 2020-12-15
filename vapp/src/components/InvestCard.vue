<template>
  <div
    id="card"
    class="bg-white bg-opacity-40 rounded-md my-4 w-5/12 flex flex-col items-center justify-center px-4 border-2 border-white border-opacity-20 border-solide"
    style="backdrop-filter: blur(10px);"
  >
    <div class="text-center mt-4">
      <h1 class="text-2xl py-5 text-gray-900">Buy Tokens</h1>
      <p id="description" class="text-l pb-5 text-gray-800">
        Choose property and token amount
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
          placeholder="Which property"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        >
          <!-- <option disabled value="">What type of property</option> -->
          <option>Property 1</option>
          <option>Property 2</option>
          <option>Property 3</option>
        </select>
        <p id="description" class="text-l pb-5 text-gray-800">
          There will be the description of the property there
        </p>
        <input
          v-model="property_address"
          type="number"
          placeholder="Number of token"
          class="bg-gray-100 appearance-none border rounded w-full py-2 px-3 text-gray-800 leading-tight focus:outline-none focus:shadow-outline"
        />

        <a href="#" class="bg-black text-white px-4 py-6 no-underline"
          >Buy tokens</a
        >
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "InvestCard",
};
</script>

<style>
/* <div class="w-full md:w-1/2 text-center md:text-right pb-4 md:p-0">
					<input type="search" placeholder="Search..." class="bg-gray-300 border text-sm p-1" />
				</div> */
</style>
