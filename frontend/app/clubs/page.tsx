import { Suspense } from "react";
import { fetchClubs } from "@/lib/api";
import ClubsList from "@/components/clubList";
import ClubsChart from "@/components/clubChart";
import { LoadingSpinner } from "@/components/ui/spinner";
import LoadableContainer from "@/components/card";

export default async function ClubsPage() {
  const clubsData = await fetchClubs();

  return (
    <div className="container mx-auto mt-4 px-4">
      <hr className="my-4" />
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <LoadableContainer>
          <h2 className="text-2xl font-normal text-gray-700  mb-4">
            Lista Klubów
          </h2>
          <ClubsList clubs={clubsData.results} />
        </LoadableContainer>
        <LoadableContainer>
          <h2 className="text-2xl font-normal text-gray-700 mb-4">
            Rozkład mandatów{" "}
          </h2>
          <ClubsChart clubs={clubsData.results} />
        </LoadableContainer>
      </div>
    </div>
  );
}
